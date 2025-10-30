# import json
# import boto3
# import uuid
# from datetime import datetime

# # AWS clients
# sqs = boto3.client('sqs')
# dynamodb = boto3.resource('dynamodb')

# # Replace with your actual resources
# SQS_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/617618117417/HealthcareBotQueue"
# DYNAMO_TABLE_NAME = "ChatbotData"

# ILLNESS_SLOT = "Illness"
# DATE_SLOT = "Date"
# TIME_SLOT = "TimeSlot"

# def lambda_handler(event, context):
#     intent_name = event['sessionState']['intent']['name']
#     slots = event['sessionState']['intent'].get('slots', {})

#     # Greeting Intent
#     if intent_name == "GreetingIntent":
#         return close("Hi, I’m your healthcare bot. How can I assist you today?")

#     # Thank You Intent
#     if intent_name == "ThankYouIntent":
#         return close("You're welcome! Stay healthy!")

#     # ServiceRequest Intent
#     if intent_name == "ServiceRequestIntent":
#         illness = get_slot(slots, ILLNESS_SLOT)
#         date = get_slot(slots, DATE_SLOT)
#         time = get_slot(slots, TIME_SLOT)

#         # Step 1: Ask for illness
#         if not illness:
#             return elicit_slot(event, ILLNESS_SLOT, "Sure, what illness do you have?")

#         # Step 2: Ask for date
#         if not date:
#             return elicit_slot(event, DATE_SLOT, f"Got it. What date would you like to schedule your appointment for {illness}?")

#         # Step 3: Ask for time
#         if not time:
#             return elicit_slot(event, TIME_SLOT, f"Okay, and what time works best for you on {date}?")

#         # Step 4: Book appointment
#         doctor = doctor_lookup(illness)
#         request_id = str(uuid.uuid4())
#         appointment_data = {
#             "RequestID": request_id,
#             "Illness": illness,
#             "Doctor": doctor,
#             "Date": date,
#             "Time": time,
#             "CreatedAt": datetime.utcnow().isoformat()
#         }

#         # Send to SQS
#         sqs.send_message(
#             QueueUrl=SQS_QUEUE_URL,
#             MessageBody=json.dumps(appointment_data)
#         )

#         # Store in DynamoDB
#         table = dynamodb.Table(DYNAMO_TABLE_NAME)
#         table.put_item(Item=appointment_data)

#         return close(
#             f"Your appointment with {doctor} has been booked for {date} at {time}. (Ref: {request_id})"
#         )

#     return close("Sorry, I didn’t understand that request.")

# # --- Helper Functions ---

# def get_slot(slots, slot_name):
#     slot = slots.get(slot_name)
#     if slot and slot.get("value"):
#         return slot["value"].get("interpretedValue")
#     return None

# def elicit_slot(event, slot_to_elicit, message):
#     return {
#         "sessionState": {
#             "dialogAction": {"type": "ElicitSlot", "slotToElicit": slot_to_elicit},
#             "intent": event['sessionState']['intent']
#         },
#         "messages": [{"contentType": "PlainText", "content": message}]
#     }

# def close(message):
#     return {
#         "sessionState": {
#             "dialogAction": {"type": "Close"},
#             "intent": {"name": "ServiceRequestIntent", "state": "Fulfilled"}
#         },
#         "messages": [{"contentType": "PlainText", "content": message}]
#     }

# def doctor_lookup(illness):
#     illness = illness.lower()
#     if "fever" in illness or "flu" in illness:
#         return "Dr. Smith (General Physician)"
#     elif "skin" in illness or "allergy" in illness:
#         return "Dr. Lee (Dermatologist)"
#     elif "cough" in illness or "breathing" in illness:
#         return "Dr. Johnson (Pulmonologist)"
#     else:
#         return "Dr. Patel (Specialist)"

## works best for all just few chnages in next code date and time parse

# import json
# import boto3
# import uuid
# from datetime import datetime

# # AWS clients
# sqs = boto3.client('sqs')
# dynamodb = boto3.resource('dynamodb')

# # Replace with your actual resources
# SQS_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/617618117417/HealthcareBotQueue"
# DYNAMO_TABLE_NAME = "ChatbotData"

# ILLNESS_SLOT = "Illness"
# DATE_SLOT = "Date"
# TIME_SLOT = "TimeSlot"

# def lambda_handler(event, context):
#     # Safety check for Lex V2 event
#     if 'sessionState' not in event:
#         return {
#             "messages": [{"contentType": "PlainText", "content": "Sorry, I didn’t understand that request."}]
#         }

#     intent_name = event['sessionState']['intent']['name']
#     slots = event['sessionState']['intent'].get('slots', {})

#     if intent_name == "GreetingIntent":
#         return close("Hi, I’m your healthcare bot. How can I assist you today?", intent_name)

#     if intent_name == "ThankYouIntent":
#         return close("You're welcome! Stay healthy!", intent_name)

#     if intent_name == "ServiceRequestIntent":
#         return handle_service_request(slots, intent_name)

#     if intent_name == "RescheduleAppointmentIntent":
#         return handle_reschedule(slots, intent_name)

#     if intent_name == "CancelAppointmentIntent":
#         return handle_cancel(intent_name)

#     return close("Sorry, I didn’t understand that request.", intent_name)


# # --- Handlers ---

# def handle_service_request(slots, intent_name):
#     illness = get_slot(slots, ILLNESS_SLOT)
#     date = get_slot(slots, DATE_SLOT)
#     time = get_slot(slots, TIME_SLOT)

#     if not illness:
#         return elicit_slot(slots, ILLNESS_SLOT, "Sure, what illness do you have?", intent_name)

#     if not date:
#         return elicit_slot(slots, DATE_SLOT, f"Got it. What date would you like to schedule your appointment for {illness}?", intent_name)

#     if not time:
#         return elicit_slot(slots, TIME_SLOT, f"Okay, and what time works best for you on {date}?", intent_name)

#     doctor = doctor_lookup(illness)
#     appointment_data = {
#         "RequestID": str(uuid.uuid4()),
#         "Illness": illness,
#         "Doctor": doctor,
#         "Date": date,
#         "Time": time,
#         "Action": "Book",
#         "CreatedAt": datetime.utcnow().isoformat()
#     }

#     send_to_sqs_and_dynamo(appointment_data)

#     return close(f"Your appointment with {doctor} has been booked for {date} at {time}.", intent_name)


# def handle_reschedule(slots, intent_name):
#     date = get_slot(slots, DATE_SLOT)
#     time = get_slot(slots, TIME_SLOT)

#     if not date:
#         return elicit_slot(slots, DATE_SLOT, "What new date would you like?", intent_name)

#     if not time:
#         return elicit_slot(slots, TIME_SLOT, "What new time works for you?", intent_name)

#     reschedule_data = {
#         "RequestID": str(uuid.uuid4()),
#         "NewDate": date,
#         "NewTime": time,
#         "Action": "Reschedule",
#         "CreatedAt": datetime.utcnow().isoformat()
#     }

#     send_to_sqs_and_dynamo(reschedule_data)

#     return close(f"Your appointment has been rescheduled to {date} at {time}.", intent_name)


# def handle_cancel(intent_name):
#     cancel_data = {
#         "RequestID": str(uuid.uuid4()),
#         "Action": "Cancel",
#         "CreatedAt": datetime.utcnow().isoformat()
#     }

#     send_to_sqs_and_dynamo(cancel_data)

#     return close("Your appointment has been cancelled.", intent_name)


# # --- Helper Functions ---

# def get_slot(slots, slot_name):
#     slot = slots.get(slot_name)
#     if slot and slot.get("value"):
#         return slot["value"].get("interpretedValue")
#     return None


# def elicit_slot(slots, slot_to_elicit, message, intent_name):
#     return {
#         "sessionState": {
#             "dialogAction": {"type": "ElicitSlot", "slotToElicit": slot_to_elicit},
#             "intent": {"name": intent_name, "slots": slots, "state": "InProgress"}
#         },
#         "messages": [{"contentType": "PlainText", "content": message}]
#     }


# def close(message, intent_name):
#     return {
#         "sessionState": {
#             "dialogAction": {"type": "Close"},
#             "intent": {"name": intent_name, "state": "Fulfilled"}
#         },
#         "messages": [{"contentType": "PlainText", "content": message}]
#     }


# def doctor_lookup(illness):
#     illness = illness.lower()
#     if "fever" in illness or "flu" in illness:
#         return "Dr. Smith (General Physician)"
#     elif "skin" in illness or "allergy" in illness:
#         return "Dr. Lee (Dermatologist)"
#     elif "cough" in illness or "breathing" in illness:
#         return "Dr. Johnson (Pulmonologist)"
#     else:
#         return "Dr. Patel (Specialist)"


# def send_to_sqs_and_dynamo(data):
#     # Send to SQS
#     sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody=json.dumps(data))

#     # Store in DynamoDB
#     table = dynamodb.Table(DYNAMO_TABLE_NAME)
#     table.put_item(Item=data)


import json
import boto3
import uuid
from datetime import datetime

# AWS clients
sqs = boto3.client('sqs')
dynamodb = boto3.resource('dynamodb')

# Resource names
SQS_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/617618117417/HealthcareBotQueue"
DOCTORS_TABLE = "DoctorsData"
APPOINTMENTS_TABLE = "ChatbotData"

ILLNESS_SLOT = "Illness"
DATE_SLOT = "Date"
TIME_SLOT = "TimeSlot"


def lambda_handler(event, context):
    # Safety check
    if 'sessionState' not in event:
        return {
            "messages": [{"contentType": "PlainText", "content": "Sorry, I didn’t understand that request."}]
        }

    intent_name = event['sessionState']['intent']['name']
    slots = event['sessionState']['intent'].get('slots', {})

    if intent_name == "GreetingIntent":
        return close("Hello! I’m your virtual health assistant — here to help you find the right doctor and to schedule, cancel, or reschedule appointments. What brings you here today?", intent_name)

    if intent_name == "ThankYouIntent":
        return close("You're welcome! Stay healthy!", intent_name)

    if intent_name == "ServiceRequestIntent":
        return handle_service_request(slots, intent_name)

    if intent_name == "RescheduleAppointmentIntent":
        return handle_reschedule(slots, intent_name)

    if intent_name == "CancelAppointmentIntent":
        return handle_cancel(intent_name)

    return close("Sorry, I didn’t understand that request.", intent_name)


# --- Handlers ---

def handle_service_request(slots, intent_name):
    illness = get_slot(slots, ILLNESS_SLOT)
    date = get_slot(slots, DATE_SLOT)
    time = get_slot(slots, TIME_SLOT)

    if not illness:
        return elicit_slot(slots, ILLNESS_SLOT, "Sure, what illness do you have?", intent_name)

    if not date:
        return elicit_slot(slots, DATE_SLOT, f"Got it. What date would you like to schedule your appointment for {illness}?", intent_name)

    if not time:
        return elicit_slot(slots, TIME_SLOT, f"Okay, and what time works best for you on {date}?", intent_name)

    doctor = doctor_lookup_from_dynamo(illness)

    if not doctor:
        return close(f"Sorry, no doctors are available for {illness} right now.", intent_name)

    appointment_data = {
        "RequestID": str(uuid.uuid4()),
        "Illness": illness,
        "DoctorID": doctor["DoctorID"],
        "DoctorName": doctor["DoctorName"],
        "Specialty": doctor["Specialty"],
        "Hospital": doctor["Hospital"],
        "Date": date,
        "Time": time,
        "Action": "Book",
        "CreatedAt": datetime.utcnow().isoformat()
    }

    send_to_sqs_and_dynamo(appointment_data)

    return close(
        f"Your appointment with {doctor['DoctorName']} ({doctor['Specialty']}) at {doctor['Hospital']} "
        f"has been booked for {date} at {time}.An email notification has also been sent confirming your appointment.",
        intent_name
    )


def handle_reschedule(slots, intent_name):
    date = get_slot(slots, DATE_SLOT)
    time = get_slot(slots, TIME_SLOT)

    if not date:
        return elicit_slot(slots, DATE_SLOT, "What new date would you like?", intent_name)

    if not time:
        return elicit_slot(slots, TIME_SLOT, "What new time works for you?", intent_name)

    reschedule_data = {
        "RequestID": str(uuid.uuid4()),
        "NewDate": date,
        "NewTime": time,
        "Action": "Reschedule",
        "CreatedAt": datetime.utcnow().isoformat()
    }

    send_to_sqs_and_dynamo(reschedule_data)

    return close(f"Your appointment has been rescheduled to {date} at {time}.", intent_name)


def handle_cancel(intent_name):
    cancel_data = {
        "RequestID": str(uuid.uuid4()),
        "Action": "Cancel",
        "CreatedAt": datetime.utcnow().isoformat()
    }

    send_to_sqs_and_dynamo(cancel_data)

    return close("Your appointment has been cancelled.", intent_name)


# --- Helper Functions ---

def get_slot(slots, slot_name):
    slot = slots.get(slot_name)
    if slot and slot.get("value"):
        return slot["value"].get("interpretedValue")
    return None


def elicit_slot(slots, slot_to_elicit, message, intent_name):
    return {
        "sessionState": {
            "dialogAction": {"type": "ElicitSlot", "slotToElicit": slot_to_elicit},
            "intent": {"name": intent_name, "slots": slots, "state": "InProgress"}
        },
        "messages": [{"contentType": "PlainText", "content": message}]
    }


def close(message, intent_name):
    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {"name": intent_name, "state": "Fulfilled"}
        },
        "messages": [{"contentType": "PlainText", "content": message}]
    }


def doctor_lookup_from_dynamo(illness):
    """
    Scans the DoctorsData table to find a doctor who treats the given illness.
    """
    table = dynamodb.Table(DOCTORS_TABLE)
    response = table.scan()

    for item in response.get('Items', []):
        illnesses = [ill.lower() for ill in item.get('Illnesses', [])]
        if illness.lower() in illnesses:
            return item
    return None


def send_to_sqs_and_dynamo(data):
    # Send message to SQS
    sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody=json.dumps(data))

    # Store booking or action in AppointmentsData table
    table = dynamodb.Table(APPOINTMENTS_TABLE)
    table.put_item(Item=data)
