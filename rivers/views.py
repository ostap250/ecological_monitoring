from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import WaterBody, WaterQualityReport, ReportFile
from .serializers import WaterBodySerializer, WaterQualityReportSerializer, ReportFileSerializer
from .fuzzy_logic import calculate_water_quality

class WaterBodyViewSet(viewsets.ModelViewSet):
    queryset = WaterBody.objects.all()
    serializer_class = WaterBodySerializer

    @action(detail=True, methods=['get'])
    def reports(self, request, pk=None):
        water_body = self.get_object()
        reports = water_body.quality_reports.all()
        serializer = WaterQualityReportSerializer(reports, many=True)
        return Response(serializer.data)

class WaterQualityReportViewSet(viewsets.ModelViewSet):
    queryset = WaterQualityReport.objects.all()
    serializer_class = WaterQualityReportSerializer

class ReportFileViewSet(viewsets.ModelViewSet):
    queryset = ReportFile.objects.all()
    serializer_class = ReportFileSerializer


class WaterQualityViewSet(viewsets.ViewSet):
    """
    ViewSet for handling water quality calculations and reports.
    """

    @action(detail=False, methods=['get'], url_path='fuzzy-water-quality')
    def fuzzy_water_quality(self, request):
        """
        Calculate water quality using fuzzy logic based on query parameters.
        """
        try:
            pollution = float(request.query_params.get('pollution', 0))
            ph = float(request.query_params.get('ph', 7))
            temperature = float(request.query_params.get('temperature', 20))

            result = calculate_water_quality(pollution, ph, temperature)

            return Response({
                "pollution": pollution,
                "ph": ph,
                "temperature": temperature,
                "quality": result
            }, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid input parameters."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='quality-reports')
    def quality_reports(self, request, pk=None):
        """
        Get water quality reports for a water body over a specified period.
        """
        try:
            # Get query parameters for date range
            start_date = request.query_params.get('start_date', None)
            end_date = request.query_params.get('end_date', None)

            # Validate the date range
            if not start_date or not end_date:
                return Response({"error": "Both start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

            # Get the water body
            water_body = WaterBody.objects.get(pk=pk)

            # Filter reports for the water body within the date range
            reports = WaterQualityReport.objects.filter(
                water_body=water_body,
                date__range=[start_date, end_date]
            )

            # Serialize the reports
            report_data = WaterQualityReportSerializer(reports, many=True).data

            # Calculate overall water quality for the period
            aggregated_quality = []
            for report in reports:
                quality = calculate_water_quality(
                    report.pollution_level,
                    report.ph_level,
                    report.temperature
                )
                aggregated_quality.append({
                    "date": report.date,
                    "quality": quality
                })

            # Serialize the related water body
            water_body_data = WaterBodySerializer(water_body).data

            # Add detailed report information and aggregated quality
            return Response({
                "water_body": water_body_data,
                "reports": report_data,
                "aggregated_quality": aggregated_quality
            }, status=status.HTTP_200_OK)

        except WaterBody.DoesNotExist:
            return Response({"error": "Water body not found."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


