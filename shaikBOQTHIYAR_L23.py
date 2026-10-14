import math
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Engineering Calculator",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Mechanical Engineering Calculator")
st.write("Select a module from the sidebar to start calculating.")

# ============================================
# SIDEBAR NAVIGATION
# ============================================
category = st.sidebar.selectbox(
    "Select Category",
    [
        "1. Mechanics",
        "2. Strength of Materials",
        "3. Thermodynamics",
        "4. Fluid Mechanics",
        "5. Thermal Engineering",
        "6. Machine Design"
    ]
)

# ============================================
# 1. MECHANICS
# ============================================
if category == "1. Mechanics":
    st.header("Mechanics")
    calculation = st.selectbox(
        "Choose Calculation",
        ["Force", "Work", "Power", "Kinetic Energy"]
    )

    if calculation == "Force":
        st.subheader("Force (F = m × a)")
        mass = st.number_input("Mass (kg)", min_value=0.001, value=10.0, step=0.1)
        acceleration = st.number_input("Acceleration (m/s²)", min_value=0.001, value=9.81, step=0.1)
        
        if st.button("Calculate Force"):
            F = mass * acceleration
            st.success(f"**Force = {F:.2f} N**")

    elif calculation == "Work":
        st.subheader("Work (W = F × d)")
        force_val = st.number_input("Force (N)", min_value=0.001, value=100.0, step=1.0)
        distance = st.number_input("Distance (m)", min_value=0.001, value=5.0, step=0.5)
        
        if st.button("Calculate Work"):
            W = force_val * distance
            st.success(f"**Work = {W:.2f} J**")

    elif calculation == "Power":
        st.subheader("Power (P = W / t)")
        work_val = st.number_input("Work Done (J)", min_value=0.001, value=500.0, step=10.0)
        time = st.number_input("Time (s)", min_value=0.001, value=10.0, step=0.5)
        
        if st.button("Calculate Power"):
            P = work_val / time
            st.success(f"**Power = {P:.2f} W**")

    elif calculation == "Kinetic Energy":
        st.subheader("Kinetic Energy (KE = ½ × m × v²)")
        mass = st.number_input("Mass (kg)", min_value=0.001, value=10.0, step=0.1)
        velocity = st.number_input("Velocity (m/s)", min_value=0.0, value=5.0, step=0.5)
        
        if st.button("Calculate Kinetic Energy"):
            KE = 0.5 * mass * (velocity ** 2)
            st.success(f"**Kinetic Energy = {KE:.2f} J**")

# ============================================
# 2. STRENGTH OF MATERIALS
# ============================================
elif category == "2. Strength of Materials":
    st.header("Strength of Materials")
    calculation = st.selectbox(
        "Choose Calculation",
        ["Stress", "Strain", "Young's Modulus"]
    )

    if calculation == "Stress":
        st.subheader("Stress (σ = F / A)")
        force_val = st.number_input("Force (N)", min_value=0.001, value=5000.0, step=100.0)
        area = st.number_input("Area (mm²)", min_value=0.001, value=50.0, step=1.0)
        
        if st.button("Calculate Stress"):
            stress_val = force_val / area
            st.success(f"**Stress = {stress_val:.2f} MPa**")

    elif calculation == "Strain":
        st.subheader("Strain (ε = ΔL / L)")
        change_l = st.number_input("Change in Length (mm)", min_value=0.001, value=0.05, step=0.01, format="%.4f")
        orig_l = st.number_input("Original Length (mm)", min_value=0.001, value=100.0, step=1.0)
        
        if st.button("Calculate Strain"):
            strain_val = change_l / orig_l
            st.success(f"**Strain = {strain_val:.6f}**")

    elif calculation == "Young's Modulus":
        st.subheader("Young's Modulus (E = σ / ε)")
        stress_val = st.number_input("Stress (MPa)", min_value=0.001, value=200.0, step=10.0)
        strain_val = st.number_input("Strain", min_value=0.000001, value=0.001, step=0.0001, format="%.6f")
        
        if st.button("Calculate Young's Modulus"):
            E = stress_val / strain_val
            st.success(f"**Young's Modulus = {E:.2f} MPa ({E / 1000:.2f} GPa)**")

# ============================================
# 3. THERMODYNAMICS
# ============================================
elif category == "3. Thermodynamics":
    st.header("Thermodynamics")
    calculation = st.selectbox(
        "Choose Calculation",
        ["Heat Transfer", "Work Done", "Thermal Efficiency"]
    )

    if calculation == "Heat Transfer":
        st.subheader("Heat Transfer (Q = m × c × ΔT)")
        mass = st.number_input("Mass (kg)", min_value=0.001, value=2.0, step=0.1)
        sp_heat = st.number_input("Specific Heat (J/kg·K)", min_value=0.001, value=4184.0, step=10.0)
        temp_diff = st.number_input("Temperature Change (K)", min_value=0.001, value=20.0, step=1.0)
        
        if st.button("Calculate Heat Transfer"):
            Q = mass * sp_heat * temp_diff
            st.success(f"**Heat Transfer = {Q:.2f} J ({Q / 1000:.2f} kJ)**")

    elif calculation == "Work Done":
        st.subheader("Thermodynamic Work (W = P × ΔV)")
        pressure = st.number_input("Pressure (Pa)", min_value=0.001, value=101325.0, step=1000.0)
        vol_change = st.number_input("Volume Change (m³)", min_value=0.001, value=0.05, step=0.01, format="%.3f")
        
        if st.button("Calculate Work Done"):
            W = pressure * vol_change
            st.success(f"**Work Done = {W:.2f} J ({W / 1000:.2f} kJ)**")

    elif calculation == "Thermal Efficiency":
        st.subheader("Thermal Efficiency (η = (Q_in - Q_out) / Q_in)")
        heat_in = st.number_input("Heat Supplied (kJ)", min_value=0.001, value=1000.0, step=50.0)
        heat_out = st.number_input("Heat Rejected (kJ)", min_value=0.0, value=400.0, step=50.0)
        
        if st.button("Calculate Efficiency"):
            if heat_out >= heat_in:
                st.error("Heat rejected must be less than heat supplied.")
            else:
                eff = ((heat_in - heat_out) / heat_in) * 100
                st.success(f"**Thermal Efficiency = {eff:.2f}%**")

# ============================================
# 4. FLUID MECHANICS
# ============================================
elif category == "4. Fluid Mechanics":
    st.header("Fluid Mechanics")
    calculation = st.selectbox(
        "Choose Calculation",
        ["Pressure", "Reynolds Number", "Flow Velocity", "Discharge"]
    )

    if calculation == "Pressure":
        st.subheader("Pressure (P = F / A)")
        force_val = st.number_input("Force (N)", min_value=0.001, value=1000.0, step=10.0)
        area = st.number_input("Area (m²)", min_value=0.001, value=0.05, step=0.01)
        
        if st.button("Calculate Pressure"):
            P = force_val / area
            st.success(f"**Pressure = {P:.2f} Pa ({P / 1000:.2f} kPa)**")

    elif calculation == "Reynolds Number":
        st.subheader("Reynolds Number (Re = ρ × v × D / μ)")
        density = st.number_input("Fluid Density (kg/m³)", min_value=0.001, value=1000.0, step=10.0)
        velocity = st.number_input("Flow Velocity (m/s)", min_value=0.001, value=1.5, step=0.1)
        diameter = st.number_input("Pipe Diameter (m)", min_value=0.001, value=0.05, step=0.01)
        viscosity = st.number_input("Dynamic Viscosity (Pa·s)", min_value=0.000001, value=0.001, step=0.0001, format="%.6f")
        
        if st.button("Calculate Reynolds Number"):
            Re = (density * velocity * diameter) / viscosity
            st.success(f"**Reynolds Number = {Re:.2f}**")
            
            if Re < 2300:
                st.info("Flow Regime: **Laminar**")
            elif Re <= 4000:
                st.warning("Flow Regime: **Transitional**")
            else:
                st.error("Flow Regime: **Turbulent**")

    elif calculation == "Flow Velocity":
        st.subheader("Flow Velocity (v = Q / A)")
        discharge_val = st.number_input("Discharge Q (m³/s)", min_value=0.001, value=0.02, step=0.005, format="%.4f")
        area = st.number_input("Cross-sectional Area (m²)", min_value=0.001, value=0.01, step=0.001, format="%.4f")
        
        if st.button("Calculate Velocity"):
            v = discharge_val / area
            st.success(f"**Flow Velocity = {v:.2f} m/s**")

    elif calculation == "Discharge":
        st.subheader("Discharge (Q = A × v)")
        area = st.number_input("Cross-sectional Area (m²)", min_value=0.001, value=0.01, step=0.001, format="%.4f")
        velocity = st.number_input("Flow Velocity (m/s)", min_value=0.001, value=2.0, step=0.1)
        
        if st.button("Calculate Discharge"):
            Q = area * velocity
            st.success(f"**Discharge = {Q:.4f} m³/s**")

# ============================================
# 5. THERMAL ENGINEERING
# ============================================
elif category == "5. Thermal Engineering":
    st.header("Thermal Engineering")
    calculation = st.selectbox(
        "Choose Calculation",
        ["Heat Conduction", "COP", "Heat Engine Efficiency"]
    )

    if calculation == "Heat Conduction":
        st.subheader("Heat Conduction (Q = k × A × ΔT / L)")
        k = st.number_input("Thermal Conductivity k (W/m·K)", min_value=0.001, value=45.0, step=1.0)
        area = st.number_input("Area (m²)", min_value=0.001, value=2.0, step=0.1)
        dT = st.number_input("Temperature Difference (K)", min_value=0.001, value=50.0, step=1.0)
        thickness = st.number_input("Thickness (m)", min_value=0.001, value=0.02, step=0.005, format="%.3f")
        
        if st.button("Calculate Conduction Rate"):
            Q = (k * area * dT) / thickness
            st.success(f"**Heat Conduction Rate = {Q:.2f} W**")

    elif calculation == "COP":
        st.subheader("Coefficient of Performance (COP = Q_cool / W_in)")
        q_cool = st.number_input("Cooling Effect (kJ)", min_value=0.001, value=15.0, step=1.0)
        w_in = st.number_input("Work Input (kJ)", min_value=0.001, value=5.0, step=0.5)
        
        if st.button("Calculate COP"):
            cop_val = q_cool / w_in
            st.success(f"**COP = {cop_val:.2f}**")

    elif calculation == "Heat Engine Efficiency":
        st.subheader("Heat Engine Efficiency (η = (Q_in - Q_out) / Q_in)")
        heat_in = st.number_input("Heat Supplied (kJ)", min_value=0.001, value=500.0, step=10.0)
        heat_out = st.number_input("Heat Rejected (kJ)", min_value=0.0, value=200.0, step=10.0)
        
        if st.button("Calculate Heat Engine Efficiency"):
            if heat_out >= heat_in:
                st.error("Heat rejected must be less than heat supplied.")
            else:
                eff = ((heat_in - heat_out) / heat_in) * 100
                st.success(f"**Heat Engine Efficiency = {eff:.2f}%**")

# ============================================
# 6. MACHINE DESIGN
# ============================================
elif category == "6. Machine Design":
    st.header("Machine Design")
    calculation = st.selectbox(
        "Choose Calculation",
        ["Torque", "Shaft Power", "Shaft Diameter"]
    )

    if calculation == "Torque":
        st.subheader("Torque (T = F × r)")
        force_val = st.number_input("Force (N)", min_value=0.001, value=250.0, step=10.0)
        radius = st.number_input("Radius / Lever Arm (m)", min_value=0.001, value=0.4, step=0.05)
        
        if st.button("Calculate Torque"):
            T = force_val * radius
            st.success(f"**Torque = {T:.2f} N·m**")

    elif calculation == "Shaft Power":
        st.subheader("Shaft Power (P = 2π × N × T / 60)")
        torque_val = st.number_input("Torque (N·m)", min_value=0.001, value=100.0, step=5.0)
        rpm = st.number_input("Speed (RPM)", min_value=0.001, value=1500.0, step=50.0)
        
        if st.button("Calculate Shaft Power"):
            P = (2 * math.pi * rpm * torque_val) / 60
            st.success(f"**Shaft Power = {P:.2f} W ({P / 1000:.2f} kW)**")

    elif calculation == "Shaft Diameter":
        st.subheader("Shaft Diameter (d = [16T / (π × τ)]^(1/3))")
        torque_val = st.number_input("Torque (N·m)", min_value=0.001, value=150.0, step=10.0)
        tau = st.number_input("Allowable Shear Stress (MPa)", min_value=0.001, value=40.0, step=5.0)
        
        if st.button("Calculate Shaft Diameter"):
            torque_nmm = torque_val * 1000
            diameter = ((16 * torque_nmm) / (math.pi * tau)) ** (1 / 3)
            st.success(f"**Shaft Diameter = {diameter:.2f} mm**")
