import yaml

from dcim.models import Site
from extras.scripts import Script, ChoiceVar
from utilities.exceptions import AbortScript


class SiteStatusFilter(Script):
    """
    Filter Sites by status.
    """
    # Define a required filter for Site status
    status = ChoiceVar(
        choices=(
            ('active', 'Active'),
            ('planned', 'Planned'),
        ),
        required=True,
        label="Site Status",
    )

    class Meta:
        name = "Site Status Filter"
        description = "List sites filtered by status."


    def run(self, data, commit):
        """
        Display sites by selected status.
        """
        # Validate data is not empty
        status = data.get('status')
        if not status:
            raise AbortScript("No status provided. Please select a valid status.")
        
        # Validate correct status
        if status not in ['active', 'planned']:
            raise AbortScript("Invalid status. Please select a valid status.")

        try:
            # Filter sites based on the selected status
            qs = Site.objects.filter(status=status).order_by("id")
            output = []

            for site in qs:
                # Log site in the UI in the required format
                self.log_info(f"#{site.id}: {site.name} - {site.get_status_display()}")
                output.append({
                    "id": site.id,
                    "name": site.name,
                    "status": site.get_status_display(),
                })

            # Display YAML format in "Output" field
            return yaml.safe_dump(output, sort_keys=False)
        
        except Exception as e:
            # Log any unexpected errors
            raise AbortScript(f"An unexpected error occurred: {str(e)}")