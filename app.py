import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence based on the given parameters.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: A list containing the arithmetic sequence
    """
    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_difference)
        sequence.append(term)
    return sequence

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title
    st.title("🔢 Arithmetic Sequence Generator")
    st.write("Generate arithmetic sequences by specifying the first term, common difference, and number of terms.")
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Parameters")
        
        # Input widgets
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            step=0.1,
            help="The first term of the arithmetic sequence"
        )
        
        common_difference = st.number_input(
            "Common Difference (d)",
            value=1.0,
            step=0.1,
            help="The constant difference between consecutive terms"
        )
        
        num_terms = st.number_input(
            "Number of Terms (n)",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (maximum 1000)"
        )
    
    with col2:
        st.subheader("Sequence Formula")
        st.latex(r"a_n = a_1 + (n-1) \cdot d")
        st.write("Where:")
        st.write("- aₙ = nth term")
        st.write("- a₁ = first term")
        st.write("- d = common difference")
        st.write("- n = term position")
    
    # Validation and sequence generation
    try:
        # Convert num_terms to integer for validation
        num_terms = int(num_terms)
        
        if num_terms <= 0:
            st.error("❌ Number of terms must be greater than 0")
            return
        
        if num_terms > 1000:
            st.error("❌ Number of terms cannot exceed 1000 for performance reasons")
            return
        
        # Generate the sequence
        sequence = generate_arithmetic_sequence(first_term, common_difference, num_terms)
        
        # Display results
        st.markdown("---")
        st.subheader("📊 Generated Sequence")
        
        # Show sequence summary
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("First Term", f"{first_term}")
        with col2:
            st.metric("Last Term", f"{sequence[-1]}")
        with col3:
            st.metric("Sum of Terms", f"{sum(sequence)}")
        
        # Display the sequence in different formats
        tab1, tab2, tab3 = st.tabs(["📋 List View", "📈 Visual Display", "🔍 Details"])
        
        with tab1:
            # Display as a formatted list
            st.write("**Sequence Terms:**")
            
            # Create a formatted string of the sequence
            if num_terms <= 50:
                # Show all terms for small sequences
                sequence_str = ", ".join([str(term) for term in sequence])
                st.code(sequence_str, language=None)
            else:
                # Show first 10, ellipsis, and last 10 for large sequences
                first_10 = ", ".join([str(term) for term in sequence[:10]])
                last_10 = ", ".join([str(term) for term in sequence[-10:]])
                sequence_str = f"{first_10}, ..., {last_10}"
                st.code(sequence_str, language=None)
                st.info(f"Showing first 10 and last 10 terms of {num_terms} total terms")
        
        with tab2:
            # Create a simple line chart for visualization
            if num_terms <= 100:  # Only show chart for reasonable number of terms
                import pandas as pd
                
                # Create DataFrame for plotting
                df = pd.DataFrame({
                    'Term Position': range(1, num_terms + 1),
                    'Value': sequence
                })
                
                st.line_chart(df.set_index('Term Position'))
                st.write("📈 Visual representation of the arithmetic sequence")
            else:
                st.info("📊 Chart not displayed for sequences with more than 100 terms")
        
        with tab3:
            # Show detailed information about the sequence
            st.write("**Sequence Details:**")
            
            # Calculate additional properties
            if num_terms > 1:
                sum_formula = f"S_n = n/2 × (2a₁ + (n-1)d) = {num_terms}/2 × (2×{first_term} + ({num_terms}-1)×{common_difference})"
                st.write(f"**Sum Formula:** {sum_formula}")
            
            st.write(f"**Arithmetic Mean:** {sum(sequence) / len(sequence):.4f}")
            
            # Show first few terms with their formulas
            st.write("**Term-by-term breakdown:**")
            for i in range(min(5, num_terms)):
                term_position = i + 1
                term_value = sequence[i]
                formula = f"a_{term_position} = {first_term} + ({term_position}-1) × {common_difference} = {term_value}"
                st.code(formula, language=None)
            
            if num_terms > 5:
                st.write("...")
                # Show the last term formula
                last_pos = num_terms
                last_value = sequence[-1]
                last_formula = f"a_{last_pos} = {first_term} + ({last_pos}-1) × {common_difference} = {last_value}"
                st.code(last_formula, language=None)
    
    except Exception as e:
        st.error(f"❌ An error occurred while generating the sequence: {str(e)}")
    
    # Additional information section
    st.markdown("---")
    st.subheader("ℹ️ About Arithmetic Sequences")
    
    with st.expander("Learn More"):
        st.write("""
        **What is an Arithmetic Sequence?**
        
        An arithmetic sequence is a sequence of numbers where the difference between consecutive terms is constant. 
        This constant difference is called the "common difference."
        
        **Examples:**
        - 2, 4, 6, 8, 10, ... (first term = 2, common difference = 2)
        - 10, 7, 4, 1, -2, ... (first term = 10, common difference = -3)
        - 5, 5, 5, 5, 5, ... (first term = 5, common difference = 0)
        
        **Key Properties:**
        - Each term can be calculated using: aₙ = a₁ + (n-1)d
        - The sum of n terms: Sₙ = n/2 × (2a₁ + (n-1)d)
        - The arithmetic mean of all terms equals (first term + last term)/2
        """)

if __name__ == "__main__":
    main()
