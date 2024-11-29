import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

all_agents = [
    "Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Fade",
    "Harbor", "Jett", "KAY/O", "Killjoy", "Neon", "Omen", "Phoenix",
    "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"
]

map_recommendations = {
    "Ascent": {"agents": ["Jett", "Killjoy", "Sova", "Omen", "KAY/O"]},
    "Bind": {"agents": ["Raze", "Brimstone", "Viper", "Cypher", "Skye"]},
    "Haven": {"agents": ["Sova", "Breach", "Astra", "Jett", "Sage"]},
    "Icebox": {"agents": ["Viper", "Sage", "Killjoy", "Reyna", "Skye"]},
    "Split": {"agents": ["Raze", "Astra", "Cypher", "Phoenix", "Sage"]},
    "Fracture": {"agents": ["Breach", "Brimstone", "Neon", "Viper", "Killjoy"]},
    "Lotus": {"agents": ["Harbor", "Viper", "Fade", "Killjoy", "Reyna"]},
    "Pearl": {"agents": ["Harbor", "Viper", "Sage", "Skye", "Chamber"]}
}

def show_team():
    selected_map = map_var.get()
    selected_main_agent = main_agent_var.get()
    
    if selected_map not in map_recommendations or selected_main_agent == "Select Your Agent":
        messagebox.showwarning("❗Peringatan❗", "Harap pilih map dan agent!")
        return

    recommendations = map_recommendations[selected_map]["agents"]
    
    other_agents = [agent for agent in recommendations if agent != selected_main_agent]
    
    messagebox.showinfo(
        "Rekomendasi Tim",
        f"Map: {selected_map}\n"
        f"Agent Utama: {selected_main_agent}\n"
        f"Tim Lainnya: {', '.join(other_agents[:4])}"
    )

def update_main_agent_options(*args):
    selected_map = map_var.get()
    if selected_map in map_recommendations:
        main_agent_menu["values"] = sorted(all_agents)
        main_agent_var.set("Select Your Agent")
    else:
        main_agent_menu["values"] = []
        main_agent_var.set("Select Your Agent")

root = tk.Tk()
root.title("Rekomendasi Agent Valorant")

title_label = tk.Label(root, text="Match Found", font=("Arial", 16))
title_label.pack(pady=10)

map_var = tk.StringVar(value="Pilih Map")
map_var.trace("w", update_main_agent_options)
map_dropdown = ttk.Combobox(root, textvariable=map_var, values=list(map_recommendations.keys()), state="readonly")
map_dropdown.pack(pady=5)

main_agent_var = tk.StringVar(value="Pilih Main Agent")
main_agent_menu = ttk.Combobox(root, textvariable=main_agent_var, state="readonly")
main_agent_menu.pack(pady=5)

team_button = tk.Button(root, text="Tampilkan Tim", command=show_team)
team_button.pack(pady=10)

root.mainloop()
