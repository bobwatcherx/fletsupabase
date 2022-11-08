import flet
from  flet import *
from flet import colors,icons
import os
from supabase import create_client, Client

def main(page:Page):
	url: str = os.environ.get("SUPABASE_URL")
	key: str = os.environ.get("SUPABASE_KEY")
	supabase: Client = create_client(url, key)
	nama = TextField(label="nama")
	kelas = TextField(label="kelas")
	listall = []
	tempapp = []
	alldata = Column()
	data = data = supabase.table("baru").select("*").execute()

	if not data :
		print("no data")
	else:
		listall.append(data)
		tempapp = listall[0].data
		for element in tempapp:
			alldata.controls.append(
				Column([
					ListTile(
                  title=Text(element["nama"]),
                  subtitle=Text(element["kelas"]),
                  trailing=IconButton(
                  	icon="create",
                  	icon_color="blue500"
                  	)
                        ),

					],alignment="center")

				)

	def addToSupabase(e):
		data = supabase.table("baru").insert(
			{"nama":nama.value,"kelas":kelas.value}
			).execute()

		alldata.controls.append(
				Column([
					ListTile(
                  title=Text(nama.value),
                  subtitle=Text(kelas.value),
                  trailing=IconButton(
                  	icon="create",
                  	icon_color="blue500"
                  	)
                        ),

					],alignment="center")

				)
		page.update()




	page.add(
		Column([
		nama,
		kelas,
		FloatingActionButton(icon="create",
			bgcolor="blue500",
			on_click=addToSupabase
			),
		alldata
			],alignment="center")
		)
	# FOR SCROLL PAGE
	page.scroll = "always"


flet.app(target=main)
