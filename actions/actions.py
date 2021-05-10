# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"



from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union, Optional, Tuple
from rasa_sdk.events import AllSlotsReset

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]



class ActionAskCouncelling(Action):

    def name(self) -> Text:
        return "action_ask_councelling"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://scontent.fdel52-1.fna.fbcdn.net/v/t1.6435-9/183182782_315349263290029_1945070212164094638_n.jpg?_nc_cat=110&ccb=1-3&_nc_sid=730e14&_nc_ohc=yKInMXifnLMAX-MlAOo&_nc_ht=scontent.fdel52-1.fna&oh=809eba20c82e5a7a7d9a9b071032e985&oe=60BCA4EA")
        dispatcher.utter_message(image="https://scontent.fdel52-1.fna.fbcdn.net/v/t1.6435-9/183739750_315349573289998_7661673750588108539_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=730e14&_nc_ohc=gaDCOnxHTLUAX_T8hNA&_nc_ht=scontent.fdel52-1.fna&oh=4564e7f13bdcf573b4a509a98ee052bb&oe=60BED535")
        dispatcher.utter_message(image="https://scontent.fdel52-1.fna.fbcdn.net/v/t1.6435-9/183078173_315349673289988_7409413171439143638_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=730e14&_nc_ohc=sXZgyVRhz90AX97qTkL&_nc_ht=scontent.fdel52-1.fna&oh=e846dca7738b0a7989cb028f80b35bb3&oe=60BB680C")
        dispatcher.utter_message(image="https://scontent.fdel52-1.fna.fbcdn.net/v/t1.6435-9/183558972_315349783289977_7895355067330214666_n.jpg?_nc_cat=103&ccb=1-3&_nc_sid=730e14&_nc_ohc=N7hbUMEFm-4AX8PkX6r&_nc_ht=scontent.fdel52-1.fna&oh=9f44b8edefe21ba4c1de63fb11f9aecf&oe=60BD93FB")
        dispatcher.utter_message(image="https://scontent.fdel52-1.fna.fbcdn.net/v/t1.6435-9/183173839_315349996623289_2894976396067456757_n.jpg?_nc_cat=100&ccb=1-3&_nc_sid=730e14&_nc_ohc=Aiu36QKG2NkAX8nysvD&_nc_ht=scontent.fdel52-1.fna&oh=947acba9bceb8f6eed75c352775eab31&oe=60BD8BD2")
        return []



class ActionHospitalBedSearch(Action):

    def name(self) -> Text:
        return "action_hospital_bed_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text=str(tracker.current_slot_values()))

        # Andhra Pradesh
        if tracker.current_slot_values()['available_city'].lower() == "andhra pradesh":
            dispatcher.utter_message(text="http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/")

        # Arunachal Pradesh
        elif tracker.current_slot_values()['available_city'].lower() == "arunachal pradesh":
            dispatcher.utter_message(text="Arunachal Pradesh govt doesn't provide any portal for live updates on bed availability.")
            dispatcher.utter_message(text="Please refer to the following helpline numbers: 0360-2214216/2214238 and +91 9485 236 624/9436 055 743")

        # Assam
        if tracker.current_slot_values()['available_city'].lower() == "assam":
            dispatcher.utter_message(text="Sorry, Assam govt doesn't provide any portal for live updates on bed availability.")

        # Bihar
        elif tracker.current_slot_values()['available_city'].lower() == "bihar":
            dispatcher.utter_message(text="https://covid19health.bihar.gov.in/DailyDashboard/BedsOccupied")

        # Chhattisgarh
        elif tracker.current_slot_values()['available_city'].lower() == "chhattisgarh":
            dispatcher.utter_message(text="https://cg.nic.in/health/covid19/RTPBedAvailable.aspx")

        # DADRA AND NAGAR HAVELI
        elif tracker.current_slot_values()['available_city'].lower() == "dadra and nagar haveli":
            dispatcher.utter_message(text="https://covidfacility.dddgov.in/")

        # DAMAN AND DIU
        elif tracker.current_slot_values()['available_city'].lower() == "daman and diu":
            dispatcher.utter_message(text="https://covidfacility.dddgov.in/")

        # Delhi
        elif tracker.current_slot_values()['available_city'].lower() == "delhi":
            dispatcher.utter_message(text="https://coronabeds.jantasamvad.org")

        # Goa
        elif tracker.current_slot_values()['available_city'].lower() == "goa":
            dispatcher.utter_message(text="https://goaonline.gov.in/beds")

        # Gujarat
        elif tracker.current_slot_values()['available_city'].lower() == "ahmedabad":
            dispatcher.utter_message(text="https://covidamd.com/")
        elif tracker.current_slot_values()['available_city'].lower() == "gandhinagar":
            dispatcher.utter_message(text="https://vmc.gov.in/HospitalModuleGMC/HospitalBedsDetails.aspx?tid=1")
        elif tracker.current_slot_values()['available_city'].lower() == "vadodara":
            dispatcher.utter_message(text="https://vmc.gov.in/Covid19VadodaraApp/CovidBedSelect.aspx")

        # HARYANA
        elif tracker.current_slot_values()['available_city'].lower() == "gurugram":
            dispatcher.utter_message(text="https://covidggn.com/public/pages/gurugram-hospitals")
        elif tracker.current_slot_values()['available_city'].lower() == "haryana":
            dispatcher.utter_message(text="https://coronaharyana.in/")

        # Himachal Pradesh
        elif tracker.current_slot_values()['available_city'].lower() == "himachal pradesh":
            dispatcher.utter_message(text="There isn't any govt. based portal for live tracking of hospital beds in J&K")
            dispatcher.utter_message(text="Please refer to the following website for covid related info of HP.")
            dispatcher.utter_message(text="http://www.nrhmhp.gov.in/content/covid-health-facilities")

        # Jammu & Kashmir
        elif tracker.current_slot_values()['available_city'].lower() == "jammu and kashmir":
            dispatcher.utter_message(text="There isn't any govt. based portal for hospital beds in J&K")
            dispatcher.utter_message(text="Please refer to the following helpline numbers: 01912520982, 0194-2440283")

        # JHARKHAND
        elif tracker.current_slot_values()['available_city'].lower() == "ranchi":
            dispatcher.utter_message(text="https://pratirakshak.co.in/new-report.php")

        # KARNATAKA
        elif tracker.current_slot_values()['available_city'].lower() == "bangalore":
            dispatcher.utter_message(text="https://bbmpgov.com/chbms/")
        elif tracker.current_slot_values()['available_city'].lower() == "karnataka":
            dispatcher.utter_message(text="https://bbmpgov.com/chbms/")

        # KERALA
        elif tracker.current_slot_values()['available_city'].lower() == "kerala":
            dispatcher.utter_message(text="https://covid19jagratha.kerala.nic.in/home/addHospitalDashBoard")

        # LADAKH
        elif tracker.current_slot_values()['available_city'].lower() == "ladakh":
            dispatcher.utter_message(text="There isn't a single bed availability portal for Ladakh. Please refer to the following website for covid related infor associated with ladakh.")
            dispatcher.utter_message(text="https://covid.ladakh.gov.in/")

        # Madhya Pradesh
        elif tracker.current_slot_values()['available_city'].lower() == "madhya pradesh":
            dispatcher.utter_message(text="http://sarthak.nhmmp.gov.in/covid/facility-bed-occupancy-dashboard/")

        # MAHARASHTRA
        elif tracker.current_slot_values()['available_city'].lower() == "nashik":
            dispatcher.utter_message(text="http://covidcbrs.nmc.gov.in/home/hospitalSummary")
        elif tracker.current_slot_values()['available_city'].lower() == "mumbai":
            dispatcher.utter_message(text="https://nmmchealthfacilities.com/HospitalInfo/showhospitalist")
        elif tracker.current_slot_values()['available_city'].lower() == "panvel":
            dispatcher.utter_message(text="https://covidbedpanvel.in/HospitalInfo/showindex")
        elif tracker.current_slot_values()['available_city'].lower() == "pune":
            dispatcher.utter_message(text="https://covidpune.com/")
        elif tracker.current_slot_values()['available_city'].lower() == "thane":
            dispatcher.utter_message(text="https://covidbedthane.in/HospitalInfo/showindex")
        elif tracker.current_slot_values()['available_city'].lower() == "ulhasnagar":
            dispatcher.utter_message(text="https://umccovidbed.in/HospitalInfo/showindex")
        elif tracker.current_slot_values()['available_city'].lower() == "maharashtra":
            dispatcher.utter_message(text="There isn't a single bed availability portal for whole of Maharashtra. Please refer to portals of following locations and choose one closest to you.")
            dispatcher.utter_message(text="NASHIK: http://covidcbrs.nmc.gov.in/home/hospitalSummary")
            dispatcher.utter_message(text="MUMBAI: https://nmmchealthfacilities.com/HospitalInfo/showhospitalist")
            dispatcher.utter_message(text="PANVEL: https://covidbedpanvel.in/HospitalInfo/showindex")
            dispatcher.utter_message(text="PUNE: https://covidpune.com/")
            dispatcher.utter_message(text="THANE: https://covidbedthane.in/HospitalInfo/showindex")
            dispatcher.utter_message(text="ULHASNAGAR: https://umccovidbed.in/HospitalInfo/showindex")

        # Manipur
        elif tracker.current_slot_values()['available_city'].lower() == "manipur":
            dispatcher.utter_message(text="There isn't any govt. based portal for hospital beds in Manipur")
            dispatcher.utter_message(text="Please refer to the following helpline numbers: 1800-3453-818, 3852411668")

        # Meghalaya
        elif tracker.current_slot_values()['available_city'].lower() == "meghalaya":
            dispatcher.utter_message(text="https://meghealth.in/MeghCare.html")

        # Mizoram
        elif tracker.current_slot_values()['available_city'].lower() == "mizoram":
            dispatcher.utter_message(text="There isn't any govt. based portal for hospital beds in Mizoram")
            dispatcher.utter_message(text="Please refer to the following helpline numbers: 0389-2323336,2322336,2318336")
            dispatcher.utter_message(text="The COVID-19 Control room contact is 1070/0389-2342520/7629072785. People can also reach out to the control room via WhatsApp on 9366331931.")

        # Nagaland
        elif tracker.current_slot_values()['available_city'].lower() == "nagaland":
            dispatcher.utter_message(text="There isn't any govt. based portal for hospital beds in Nagaland")
            dispatcher.utter_message(text="Please refer to the following helpline numbers: 0370-227003, 7005539653")

        # ODISHA
        elif tracker.current_slot_values()['available_city'].lower() == "koraput":
            dispatcher.utter_message(text="https://koraput.nic.in/beds-availability-in-hospitals/")
        elif tracker.current_slot_values()['available_city'].lower() == "odisha":
            #dispatcher.utter_message(text="There isn't a single bed availability portal for whole of Odisha. Please refer to portal of Koraput in Odisha.")
            dispatcher.utter_message(text="https://statedashboard.odisha.gov.in/")

        # PUNJAB
        elif tracker.current_slot_values()['available_city'].lower() == "ludhiana":
            dispatcher.utter_message(text="http://hbmsludhiana.in/index_app_detail.php?type=all")

        # RAJASTHAN
        elif tracker.current_slot_values()['available_city'].lower() == "rajasthan":
            dispatcher.utter_message(text="https://covidinfo.rajasthan.gov.in/Covid-19hospital-wisebedposition-wholeRajasthan.aspx")

        # Tamil Nadu
        elif tracker.current_slot_values()['available_city'].lower() == "tamil nadu":
            dispatcher.utter_message(text="https://stopcorona.tn.gov.in/beds.php")

        # TELANGANA
        elif tracker.current_slot_values()['available_city'].lower() == "telangana":
            dispatcher.utter_message(text="http://164.100.112.24/SpringMVC/Hospital_Beds_Statistic_Bulletin_citizen.html")

        # Tripura
        elif tracker.current_slot_values()['available_city'].lower() == "tripura":
            dispatcher.utter_message(text="There isn't any govt. based portal for hospital beds in Tripura")
            dispatcher.utter_message(text="Please refer to the following helpline numbers: 0381-2315879, 2412424, 2413434, 2410111, 2411622 and 8414-969-592")

        # UTTARAKHAND
        elif tracker.current_slot_values()['available_city'].lower() == "uttarakhand":
            dispatcher.utter_message(text="https://covid19.uk.gov.in/bedssummary.aspx")

        # UTTAR PRADESH
        elif tracker.current_slot_values()['available_city'].lower() == "uttar pradesh":
            dispatcher.utter_message(text="https://beds.dgmhup-covid19.in/EN/covid19bedtrack")

        # WB
        elif tracker.current_slot_values()['available_city'].lower() == "west bengal":
            dispatcher.utter_message(text="https://excise.wb.gov.in/chms/Public/Page/CHMS_Public_Hospital_Bed_Availability.aspx")


        else:
            dispatcher.utter_message(text="Sorry, we currently don't have any data associated with your city/state.")

        return []

