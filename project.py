class Hospital:
    all_doctors ={}
    appointments={}

    def __init__(self, name,specialize, appointment):
        self.name = name
        self.specialize = specialize
        self.appointment = appointment
        Hospital.all_doctors[self.name]=[self.specialize]
        Hospital.appointments[self.name]={}

    @classmethod
    def get_doctors_by_specialize(cls,specialize):
        x=[]
        for i in cls.all_doctors.values():
            if i==specialize:
                x.append(str(i))
                print(f"the doctors who specialize at {cls,specialize} are {str(x)}")

    @classmethod
    def book (cls,doctor_name,time,patient_name):
        while True:
            try:
                s=int(time)
                x=doctor_name
                z=patient_name
                if s > 24:
                    print("you have entered a time more than 24")
                    break

                for i in Hospital.appointments:
                    if i==x:
                        if Hospital.appointments[i]=="":
                            Hospital.appointments[i].append([z,s])
                        else:
                            for c in Hospital.appointments[i]:
                                if s==c:
                                    print(f"I'm sorry,the doctor have an appointment in this time")
                                    return
                                elif s!=c:
                                    Hospital.appointments[i].append([z,s])
                                    print(f"{patient_name} appointment will be at {s}")
                    break
            except ValueError:
                print(f"you have used a wrong data type ")
                break


    @classmethod
    def view (cls,doctor_name):
        if doctor_name  not in Hospital.appointments:
            print(f"the name {doctor_name} is not found")
            return
        else:
            for i in Hospital.appointments:
                if i==doctor_name:
                    print(f"{Hospital.appointments[i]} have appointments at {Hospital.appointments[i].values()}")

    @classmethod
    def available(cls,time):
        x = []
        for i in Hospital.appointments:
            if Hospital.appointments[i].values()!= time :
                x.append(Hospital.appointments[i])
        print(f"the doctors who are free are {x}")

    def __str__(self):
        print(f"{self.name} from {self.specialize}")




