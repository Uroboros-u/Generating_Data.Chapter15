import plotly.express as px
import pandas as pd
from pathlib import(Path)
import json


class DJinni:
    def __init__(self):
        self.candidates = None
        self.jobs = None
        self.path = Path('dataset.json')

        self.statistics = []


    def add_statistics(self):
        while True:
            print("Would you like to add statistics? (y/n)")
            choice = input().lower()
            if choice == "y":
                date_raw = input("date dd.mm.yyyy' : ")
                clean = date_raw.strip()
                date = clean.replace(" ", "")

                cand_raw = input("candidates: ")
                cand = self._validator(cand_raw)
                cand = int(cand)

                jobs_raw = input("jobs: ")
                job = self._validator(jobs_raw)
                jobs = int(job)

                self._add_data(date, cand, jobs)
            elif choice == "n":
                break


    def _validator(self, string):
        clean = string.strip()
        clean = clean.replace(",", "")
        clean = clean.replace(" ", "")
        clean = clean.replace(".", "")
        return clean

    def _add_data(self,date, candidates, jobs):
        statistics = {"date":date, "candidates": candidates, "jobs": jobs}
        self.statistics.append(statistics)


    def next_step(self):
        des = (input('What will we do? Create a new file or add info in exist file? (c/a) ')).lower()
        if des == "c":
            dataset = json.dumps(stat.statistics)
            self.path.write_text(dataset)
        elif des == "a":
            if self.path.exists():
                with open(self.path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                    except json.decoder.JSONDecodeError:
                        data = []
            else:
                data = []

            data.extend(stat.statistics)

            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

        elif des == "q":
            pass

    def read_data(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []
            return data


stat = DJinni()
# stat.add_statistics()
# stat.next_step()
data = stat.read_data()

df= pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')

fig = px.bar(df, x="date", y=["jobs", "candidates"], barmode="group", title="Candidates vs Jobs over Time")


# fig.write_html('Job_statistics.html')
fig.show()

