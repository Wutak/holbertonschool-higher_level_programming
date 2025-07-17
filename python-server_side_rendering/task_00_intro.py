import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error("Invalid template type. Expected a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid attendees input. Expected a list of dictionaries.")
        return

    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        filled_template = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            filled_template = filled_template.replace("{" + placeholder + "}", str(value))

        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(filled_template)
            logging.info(f"Generated {output_filename}")
        except Exception as e:
            logging.error(f"Failed to write {output_filename}: {e}")
