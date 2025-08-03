import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon as MplPolygon
import plotly.graph_objects as go
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Polygon Explorer",
    page_icon="🔺",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .polygon-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .property-box {
        background: #e3f2fd;
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header"><h1>🔺 Polygon Explorer - Interactive Learning Tool</h1><p>Discover the fascinating world of polygons and their properties!</p></div>', unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("📚 Learning Modules")
module = st.sidebar.selectbox(
    "Choose a learning module:",
    ["Introduction to Polygons", "Regular Polygons Explorer", "Polygon Properties Calculator", "Quiz & Activities", "Polygon Art Creator"]
)

def calculate_polygon_properties(n_sides, side_length=1):
    """Calculate properties of a regular polygon"""
    if n_sides < 3:
        return None
    
    # Interior angle
    interior_angle = (n_sides - 2) * 180 / n_sides
    
    # Exterior angle
    exterior_angle = 360 / n_sides
    
    # Perimeter
    perimeter = n_sides * side_length
    
    # Area (for regular polygon)
    apothem = side_length / (2 * math.tan(math.pi / n_sides))
    area = 0.5 * perimeter * apothem
    
    # Central angle
    central_angle = 360 / n_sides
    
    return {
        'interior_angle': interior_angle,
        'exterior_angle': exterior_angle,
        'perimeter': perimeter,
        'area': area,
        'central_angle': central_angle,
        'apothem': apothem
    }

def create_regular_polygon(n_sides, center=(0, 0), radius=1):
    """Create coordinates for a regular polygon"""
    angles = np.linspace(0, 2*np.pi, n_sides + 1)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y

def plot_polygon_matplotlib(n_sides, side_length=1):
    """Plot polygon using matplotlib"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    # Calculate radius for regular polygon
    radius = side_length / (2 * math.sin(math.pi / n_sides))
    
    x, y = create_regular_polygon(n_sides, radius=radius)
    
    # Plot polygon
    polygon = MplPolygon(list(zip(x[:-1], y[:-1])), 
                        facecolor='lightblue', 
                        edgecolor='navy', 
                        linewidth=2,
                        alpha=0.7)
    ax.add_patch(polygon)
    
    # Add vertex labels
    for i in range(n_sides):
        ax.plot(x[i], y[i], 'ro', markersize=8)
        ax.annotate(f'V{i+1}', (x[i], y[i]), 
                   xytext=(10, 10), textcoords='offset points',
                   fontsize=12, fontweight='bold')
    
    # Add center point
    ax.plot(0, 0, 'ko', markersize=8)
    ax.annotate('Center', (0, 0), 
               xytext=(10, -20), textcoords='offset points',
               fontsize=12, fontweight='bold')
    
    ax.set_xlim(-radius*1.5, radius*1.5)
    ax.set_ylim(-radius*1.5, radius*1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title(f'Regular {n_sides}-sided Polygon', fontsize=16, fontweight='bold')
    
    return fig

def plot_polygon_plotly(n_sides, side_length=1):
    """Plot polygon using plotly for better interactivity"""
    radius = side_length / (2 * math.sin(math.pi / n_sides))
    x, y = create_regular_polygon(n_sides, radius=radius)
    
    fig = go.Figure()
    
    # Add polygon
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines+markers',
        fill='toself',
        fillcolor='rgba(100, 150, 255, 0.3)',
        line=dict(color='navy', width=3),
        marker=dict(size=10, color='red'),
        name=f'{n_sides}-sided polygon'
    ))
    
    # Add vertex labels
    for i in range(n_sides):
        fig.add_annotation(
            x=x[i], y=y[i],
            text=f'V{i+1}',
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="black"
        )
    
    # Add center point
    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers',
        marker=dict(size=12, color='black'),
        name='Center'
    ))
    
    fig.update_layout(
        title=f'Regular {n_sides}-sided Polygon',
        xaxis_title='X',
        yaxis_title='Y',
        showlegend=True,
        width=600,
        height=600
    )
    
    fig.update_xaxes(scaleanchor="y", scaleratio=1)
    
    return fig

# Module 1: Introduction to Polygons
if module == "Introduction to Polygons":
    st.header("📐 What is a Polygon?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="polygon-card">
        <h3>Definition</h3>
        <p>A polygon is a closed figure made up of straight line segments called sides. 
        Each side connects two vertices (corner points).</p>
        
        <h3>Key Characteristics:</h3>
        <ul>
        <li><strong>Closed shape:</strong> The sides form a complete loop</li>
        <li><strong>Straight sides:</strong> No curved lines</li>
        <li><strong>Vertices:</strong> Corner points where sides meet</li>
        <li><strong>Angles:</strong> Formed at each vertex</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="property-box">
        <h4>Types of Polygons by Sides:</h4>
        <ul>
        <li>3 sides: Triangle</li>
        <li>4 sides: Quadrilateral</li>
        <li>5 sides: Pentagon</li>
        <li>6 sides: Hexagon</li>
        <li>7 sides: Heptagon</li>
        <li>8 sides: Octagon</li>
        <li>9 sides: Nonagon</li>
        <li>10 sides: Decagon</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("🎯 Interactive Demo")
    demo_sides = st.slider("Choose number of sides:", 3, 12, 6)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = plot_polygon_plotly(demo_sides)
        st.plotly_chart(fig, use_container_width=True, key="intro_demo_plot")
    
    with col2:
        props = calculate_polygon_properties(demo_sides)
        st.markdown(f"""
        <div class="property-box">
        <h4>Properties of this {demo_sides}-sided polygon:</h4>
        <p><strong>Number of vertices:</strong> {demo_sides}</p>
        <p><strong>Number of sides:</strong> {demo_sides}</p>
        <p><strong>Sum of interior angles:</strong> {(demo_sides-2)*180}°</p>
        <p><strong>Each interior angle:</strong> {props['interior_angle']:.1f}°</p>
        <p><strong>Each exterior angle:</strong> {props['exterior_angle']:.1f}°</p>
        </div>
        """, unsafe_allow_html=True)

# Module 2: Regular Polygons Explorer
elif module == "Regular Polygons Explorer":
    st.header("⭐ Regular Polygons Explorer")
    
    st.markdown("""
    <div class="polygon-card">
    <h3>What makes a polygon "regular"?</h3>
    <p>A regular polygon has:</p>
    <ul>
    <li><strong>Equal sides:</strong> All sides have the same length</li>
    <li><strong>Equal angles:</strong> All interior angles are the same</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🎛️ Controls")
        n_sides = st.slider("Number of sides:", 3, 20, 6, key="explorer_sides")
        side_length = st.slider("Side length:", 0.5, 3.0, 1.0, 0.1, key="explorer_length")
        
        show_measurements = st.checkbox("Show measurements", value=True)
        show_center = st.checkbox("Show center and apothem", value=False)
    
    with col2:
        st.subheader("📊 Properties")
        props = calculate_polygon_properties(n_sides, side_length)
        
        st.metric("Interior Angle", f"{props['interior_angle']:.2f}°")
        st.metric("Exterior Angle", f"{props['exterior_angle']:.2f}°")
        st.metric("Perimeter", f"{props['perimeter']:.2f}")
        st.metric("Area", f"{props['area']:.2f}")
        st.metric("Apothem", f"{props['apothem']:.2f}")
    
    # Large visualization
    st.subheader("🔍 Visualization")
    fig = plot_polygon_plotly(n_sides, side_length)
    st.plotly_chart(fig, use_container_width=True, key="explorer_main_plot")
    
    # Formulas
    st.subheader("📝 Formulas for Regular Polygons")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="property-box">
        <h4>Angle Formulas:</h4>
        <p><strong>Interior Angle:</strong> (n-2) × 180° / n</p>
        <p><strong>Exterior Angle:</strong> 360° / n</p>
        <p><strong>Central Angle:</strong> 360° / n</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="property-box">
        <h4>Measurement Formulas:</h4>
        <p><strong>Perimeter:</strong> n × side length</p>
        <p><strong>Apothem:</strong> s / (2 × tan(π/n))</p>
        <p><strong>Area:</strong> (1/2) × perimeter × apothem</p>
        </div>
        """, unsafe_allow_html=True)

# Module 3: Polygon Properties Calculator
elif module == "Polygon Properties Calculator":
    st.header("🧮 Polygon Properties Calculator")
    
    st.markdown("""
    <div class="polygon-card">
    <h3>Calculate properties of any regular polygon!</h3>
    <p>Enter the number of sides and one measurement to calculate all other properties.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Input Parameters")
        calc_sides = st.number_input("Number of sides:", min_value=3, max_value=50, value=6)
        
        input_type = st.selectbox(
            "What do you know?",
            ["Side Length", "Perimeter", "Area", "Apothem"]
        )
        
        if input_type == "Side Length":
            known_value = st.number_input("Side length:", min_value=0.1, value=1.0, step=0.1)
            side_length = known_value
        elif input_type == "Perimeter":
            known_value = st.number_input("Perimeter:", min_value=0.1, value=6.0, step=0.1)
            side_length = known_value / calc_sides
        elif input_type == "Area":
            known_value = st.number_input("Area:", min_value=0.1, value=2.6, step=0.1)
            # Calculate side length from area (approximation)
            apothem_est = math.sqrt(known_value * 2 / calc_sides / math.tan(math.pi / calc_sides))
            side_length = 2 * apothem_est * math.tan(math.pi / calc_sides)
        else:  # Apothem
            known_value = st.number_input("Apothem:", min_value=0.1, value=0.87, step=0.01)
            side_length = 2 * known_value * math.tan(math.pi / calc_sides)
    
    with col2:
        st.subheader("📊 Calculated Properties")
        
        if calc_sides >= 3:
            props = calculate_polygon_properties(calc_sides, side_length)
            
            col2a, col2b = st.columns(2)
            
            with col2a:
                st.metric("Number of Sides", calc_sides)
                st.metric("Side Length", f"{side_length:.3f}")
                st.metric("Perimeter", f"{props['perimeter']:.3f}")
                st.metric("Area", f"{props['area']:.3f}")
            
            with col2b:
                st.metric("Apothem", f"{props['apothem']:.3f}")
                st.metric("Interior Angle", f"{props['interior_angle']:.2f}°")
                st.metric("Exterior Angle", f"{props['exterior_angle']:.2f}°")
                st.metric("Central Angle", f"{props['central_angle']:.2f}°")
    
    # Visualization
    if calc_sides >= 3:
        st.subheader("📐 Polygon Visualization")
        fig = plot_polygon_plotly(calc_sides, side_length)
        st.plotly_chart(fig, use_container_width=True, key="calculator_plot")

# Module 4: Quiz & Activities
elif module == "Quiz & Activities":
    st.header("🎯 Quiz & Activities")
    
    # Initialize session state for quiz
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'quiz_question' not in st.session_state:
        st.session_state.quiz_question = 0
    
    tab1, tab2, tab3 = st.tabs(["Quick Quiz", "Angle Hunt", "Property Match"])
    
    with tab1:
        st.subheader("🧠 Quick Quiz")
        
        quiz_questions = [
            {
                "question": "What is the sum of interior angles in a pentagon?",
                "options": ["360°", "540°", "720°", "900°"],
                "correct": 1,
                "explanation": "Formula: (n-2) × 180° = (5-2) × 180° = 540°"
            },
            {
                "question": "How many sides does a decagon have?",
                "options": ["8", "9", "10", "12"],
                "correct": 2,
                "explanation": "Decagon means 10 sides (deca = ten)"
            },
            {
                "question": "What is each exterior angle of a regular hexagon?",
                "options": ["45°", "60°", "90°", "120°"],
                "correct": 1,
                "explanation": "Each exterior angle = 360° ÷ 6 = 60°"
            }
        ]
        
        if st.session_state.quiz_question < len(quiz_questions):
            q = quiz_questions[st.session_state.quiz_question]
            st.write(f"**Question {st.session_state.quiz_question + 1}:** {q['question']}")
            
            answer = st.radio("Choose your answer:", q['options'], key=f"q{st.session_state.quiz_question}")
            
            if st.button("Submit Answer"):
                if q['options'].index(answer) == q['correct']:
                    st.success("Correct! 🎉")
                    st.session_state.quiz_score += 1
                else:
                    st.error(f"Incorrect. The correct answer is: {q['options'][q['correct']]}")
                
                st.info(f"**Explanation:** {q['explanation']}")
                st.session_state.quiz_question += 1
                
                if st.session_state.quiz_question >= len(quiz_questions):
                    st.balloons()
                    st.success(f"Quiz Complete! Your score: {st.session_state.quiz_score}/{len(quiz_questions)}")
        else:
            st.success(f"Quiz Complete! Your final score: {st.session_state.quiz_score}/{len(quiz_questions)}")
            if st.button("Restart Quiz"):
                st.session_state.quiz_score = 0
                st.session_state.quiz_question = 0
                st.rerun()
    
    with tab2:
        st.subheader("🔍 Angle Hunt")
        st.write("Find the missing angles in these polygons!")
        
        hunt_sides = st.selectbox("Choose polygon:", [3, 4, 5, 6, 8], key="hunt")
        
        props = calculate_polygon_properties(hunt_sides)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = plot_polygon_plotly(hunt_sides)
            st.plotly_chart(fig, use_container_width=True, key="angle_hunt_plot")
        
        with col2:
            st.write("**Given information:**")
            st.write(f"- This is a regular {hunt_sides}-sided polygon")
            st.write(f"- All sides are equal")
            st.write(f"- All angles are equal")
            
            user_interior = st.number_input("What is each interior angle?", value=0.0, step=0.1)
            user_exterior = st.number_input("What is each exterior angle?", value=0.0, step=0.1)
            
            if st.button("Check Answers", key="angle_check"):
                interior_correct = abs(user_interior - props['interior_angle']) < 0.1
                exterior_correct = abs(user_exterior - props['exterior_angle']) < 0.1
                
                if interior_correct and exterior_correct:
                    st.success("Perfect! Both angles are correct! 🎯")
                elif interior_correct:
                    st.warning("Interior angle is correct, but check the exterior angle.")
                elif exterior_correct:
                    st.warning("Exterior angle is correct, but check the interior angle.")
                else:
                    st.error("Both angles need adjustment. Try again!")
                
                st.info(f"**Correct answers:** Interior = {props['interior_angle']:.1f}°, Exterior = {props['exterior_angle']:.1f}°")
    
    with tab3:
        st.subheader("🎲 Property Match")
        st.write("Match the polygon with its properties!")
        
        polygons_data = [
            {"name": "Triangle", "sides": 3, "interior": 60, "sum_interior": 180},
            {"name": "Square", "sides": 4, "interior": 90, "sum_interior": 360},
            {"name": "Pentagon", "sides": 5, "interior": 108, "sum_interior": 540},
            {"name": "Hexagon", "sides": 6, "interior": 120, "sum_interior": 720},
            {"name": "Octagon", "sides": 8, "interior": 135, "sum_interior": 1080}
        ]
        
        selected_polygon = st.selectbox("Choose a polygon:", [p["name"] for p in polygons_data])
        
        polygon_info = next(p for p in polygons_data if p["name"] == selected_polygon)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = plot_polygon_plotly(polygon_info["sides"])
            st.plotly_chart(fig, use_container_width=True, key="property_match_plot")
        
        with col2:
            st.write(f"**Properties of a regular {selected_polygon}:**")
            st.write(f"🔹 Number of sides: {polygon_info['sides']}")
            st.write(f"🔹 Each interior angle: {polygon_info['interior']}°")
            st.write(f"🔹 Sum of interior angles: {polygon_info['sum_interior']}°")
            st.write(f"🔹 Each exterior angle: {360/polygon_info['sides']}°")

# Module 5: Polygon Art Creator
elif module == "Polygon Art Creator":
    st.header("🎨 Polygon Art Creator")
    
    st.markdown("""
    <div class="polygon-card">
    <h3>Create Beautiful Polygon Art!</h3>
    <p>Combine multiple polygons to create interesting patterns and designs.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎛️ Art Controls")
        
        num_polygons = st.slider("Number of polygons:", 1, 5, 3)
        
        polygons = []
        colors = ['red', 'blue', 'green', 'orange', 'purple']
        
        for i in range(num_polygons):
            st.write(f"**Polygon {i+1}:**")
            sides = st.slider(f"Sides:", 3, 12, 6, key=f"art_sides_{i}")
            size = st.slider(f"Size:", 0.3, 2.0, 1.0, 0.1, key=f"art_size_{i}")
            rotation = st.slider(f"Rotation:", 0, 360, 0, 15, key=f"art_rotation_{i}")
            
            polygons.append({
                'sides': sides,
                'size': size,
                'rotation': rotation,
                'color': colors[i % len(colors)]
            })
    
    with col2:
        st.subheader("🖼️ Your Polygon Art")
        
        fig = go.Figure()
        
        # Define color palette
        color_palette = [
            'rgba(255, 99, 132, 0.4)',    # Red
            'rgba(54, 162, 235, 0.4)',    # Blue  
            'rgba(75, 192, 192, 0.4)',    # Green
            'rgba(255, 205, 86, 0.4)',    # Yellow
            'rgba(153, 102, 255, 0.4)'    # Purple
        ]
        
        line_colors = [
            'rgb(255, 99, 132)',    # Red
            'rgb(54, 162, 235)',    # Blue  
            'rgb(75, 192, 192)',    # Green
            'rgb(255, 205, 86)',    # Yellow
            'rgb(153, 102, 255)'    # Purple
        ]
        
        for i, poly in enumerate(polygons):
            radius = poly['size']
            angles = np.linspace(0, 2*np.pi, poly['sides'] + 1) + np.radians(poly['rotation'])
            x = radius * np.cos(angles)
            y = radius * np.sin(angles)
            
            fig.add_trace(go.Scatter(
                x=x, y=y,
                mode='lines',
                fill='toself',
                fillcolor=color_palette[i % len(color_palette)],
                line=dict(color=line_colors[i % len(line_colors)], width=2),
                name=f'Polygon {i+1} ({poly["sides"]} sides)',
                showlegend=True
            ))
        
        fig.update_layout(
            title="Your Polygon Art Creation",
            xaxis_title="X",
            yaxis_title="Y",
            showlegend=True,
            width=500,
            height=500,
            xaxis=dict(range=[-3, 3]),
            yaxis=dict(range=[-3, 3])
        )
        
        fig.update_xaxes(scaleanchor="y", scaleratio=1)
        
        st.plotly_chart(fig, use_container_width=True, key="polygon_art_plot")
        
        if st.button("🎲 Random Art"):
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
<p>🔺 Polygon Explorer - Making geometry fun and interactive! 🔺</p>
<p>Built with ❤️ for high school students</p>
</div>
""", unsafe_allow_html=True)
