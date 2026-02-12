from __future__ import annotations

from nicegui import ui


def generate_feedback(instructor_message: str, learner_response: str) -> str:
    """Connect the instructor guidance with the learner response."""
    instructor = instructor_message.strip()
    learner = learner_response.strip()

    if not instructor or not learner:
        return 'Add both an instructor prompt and a learner response to receive connected feedback.'

    cues = {
        'pause': 'Use short pauses to let the audience process the emotional subtext.',
        'tone': 'Vary your tone to highlight meaning that is implied rather than spoken.',
        'story': 'Anchor your delivery in a concrete story moment so listeners feel the hidden stakes.',
        'gesture': 'Support key moments with intentional gestures to reinforce unspoken intent.',
        'audience': 'Keep eye contact to read how the audience reacts to subtle meaning.',
        'silence': 'Treat silence as part of the message; it can reveal confidence and depth.',
        'emotion': 'Name the emotion internally before speaking so it comes through naturally.',
    }

    matched_tips = [tip for keyword, tip in cues.items() if keyword in f'{instructor.lower()} {learner.lower()}']
    if not matched_tips:
        matched_tips = [
            'Translate the instructor\'s direction into one specific action in your next spoken sentence.',
            'When telling the story, emphasize what is felt but not directly said.',
        ]

    return (
        'Connection Feedback:\n\n'
        f'Instructor focus: "{instructor}"\n'
        f'Learner response: "{learner}"\n\n'
        'What aligns:\n'
        '- You are working on storytelling to make listeners hear meaning beneath the words.\n\n'
        'Next improvement step:\n'
        f'- {matched_tips[0]}\n'
        f'- {matched_tips[-1]}\n\n'
        'Practice prompt:\n'
        '- Retell the same moment in 30 seconds and intentionally stress one unsaid emotion through pace, pause, and vocal color.'
    )


def on_generate() -> None:
    feedback.value = generate_feedback(instructor_input.value, learner_input.value)


ui.page_title('Public Speaking Story Coach')

with ui.column().classes('w-full max-w-3xl mx-auto p-6 gap-4'):
    ui.label('Instructor ↔ Learner Conversation Coach').classes('text-2xl font-bold')
    ui.label(
        'Train public speaking through storytelling: focus on the unsaid elements that carry value.'
    ).classes('text-base text-gray-700')

    instructor_input = ui.textarea(
        label='Instructor: Describe what the learner should do',
        placeholder='Example: Tell the story of your first presentation and pause before the turning point.',
    ).props('outlined autogrow')

    learner_input = ui.textarea(
        label='Learner: Provide your response',
        placeholder='Example: I would start calmly, then pause before sharing what I learned from failure.',
    ).props('outlined autogrow')

    ui.button('Generate AI Connection Feedback', on_click=on_generate).props('color=primary')

    feedback = ui.textarea(
        label='AI Agent Feedback',
        placeholder='Feedback will appear here...',
    ).props('outlined readonly autogrow')


ui.run(host='0.0.0.0', port=8080, title='Storytelling Public Speaking Trainer')
