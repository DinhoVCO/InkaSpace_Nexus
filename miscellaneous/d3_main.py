import streamlit as st
from components.chatbot import chatbot_interface
from agents.agent_mission_architects import graph  # your compiled graph
from markdown_pdf import MarkdownPdf
from markdown_pdf import Section
import io
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage
from utils.prompts import MISSION_CONCEPT_PROMPT_TEMPLATE_EN

llm = ChatMistralAI(
    model="open-mixtral-8x7b",
    temperature=0,
    max_retries=2,
)

pdf = MarkdownPdf(toc_level=2, optimize=True)


def render_main_content(user_type):
    """Muestra el contenido de la página principal del dashboard."""
    col1, col2, col3 = st.columns([1.5, 4, 1.5])

    with col1:
        # --- NUEVO: Selector de tipo de prompt ---
        st.header("Agent Mission Architect Type")
        prompt_type = st.radio(
            "Choose AI prompt",
            ("Simple", "Strict"),
            index=0,
            key="prompt_type_selector"
        )

    with col3:
        st.header("Report Generation")
        
        if st.button("🔬 Generate Research Summary"):
            if "messages_d3" in st.session_state and st.session_state.messages_d3:
                with st.spinner("Analyzing conversation and generating AI report... This may take a moment."):
                    # 1. Formatear la conversación completa en un solo string
                    transcript_list = []
                    for msg in st.session_state.messages_d3:
                        role = "Researcher (User)" if msg["role"] == "user" else "AI Assistant"
                        transcript_list.append(f"**{role}:**\n{msg['content']}\n")
                    conversation_transcript = "\n---\n".join(transcript_list)

                    # 2. Preparar el prompt y los mensajes para el LLM
                    final_prompt = MISSION_CONCEPT_PROMPT_TEMPLATE_EN.format(conversation_transcript=conversation_transcript)
                    messages = [HumanMessage(content=final_prompt)]

                    # 3. Invocar el LLM para generar el reporte
                    try:
                        ai_report_content = llm.invoke(messages).content

                        # 4. Generar el PDF a partir de la respuesta del LLM
                        pdf = MarkdownPdf(toc_level=2)
                        pdf.add_section(Section(ai_report_content, toc=False))
                        
                        pdf_buffer = io.BytesIO()
                        pdf.save(pdf_buffer)
                        
                        # 5. Guardar en session_state para la descarga
                        st.session_state.pdf_summary_bytes = pdf_buffer.getvalue()
                        st.success("AI Research Summary is ready for download!")

                    except Exception as e:
                        st.error(f"Failed to generate report: {e}")
            else:
                st.warning("The conversation is empty. Please chat first.")

        # Botón de descarga para el reporte generado por IA
        if 'pdf_summary_bytes' in st.session_state and st.session_state.pdf_summary_bytes:
            st.download_button(
                label="✅ Download AI Summary PDF",
                data=st.session_state.pdf_summary_bytes,
                file_name="ai_research_summary.pdf",
                mime="application/pdf",
            )

            

    with col2:
        st.header("🤖 AI CHATBOT ")
        if "messages_d3" not in st.session_state:
            st.session_state.messages_d3 = [
                {"role": "assistant", "content": "Hello! How can I help you today?"}
            ]
        # Pasa las secciones seleccionadas a tu chatbot si es necesario
        chatbot_interface(st.session_state.messages_d3, graph, prompt_type=st.session_state.prompt_type_selector)