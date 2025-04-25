from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Função de boas-vindas
async def start(update: Update, context: CallbackContext) -> int:
    user_name = update.effective_user.first_name
    welcome_message = f"Olá {user_name},\n\nSeja bem-vindo ao nosso ambiente de aprendizado! Este espaço foi criado para estender seus conhecimentos em áreas como marketing, gestão de pessoas, estética avançada, engenharia e arquitetura. Vamos começar?"
    
    keyboard = [
        [InlineKeyboardButton("Iniciar", callback_data='iniciar')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

    return 1

# Função de seleção de trilhas
async def trilha(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Marketing", callback_data='marketing')],
        [InlineKeyboardButton("Gestão de Pessoas", callback_data='gestao_pessoas')],
        [InlineKeyboardButton("Estética Avançada", callback_data='estetica_avancada')],
        [InlineKeyboardButton("Engenharia", callback_data='engenharia')],
        [InlineKeyboardButton("Arquitetura", callback_data='arquitetura')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    texto = "Escolha a trilha de conhecimento que você deseja explorar:"
    await query.edit_message_text(text=texto, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

    return 2

# Função de links da trilha
async def mostrar_links(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    trilha = query.data
    links = {
        'marketing': [
            "https://link-artigo-marketing-1.com",
            "https://link-artigo-marketing-2.com",
            "https://link-video-marketing.com",
            "https://link-artigo-marketing-3.com",
            "https://link-video-marketing-2.com"
        ],
        'gestao_pessoas': [
            "https://link-artigo-gestao-pessoas-1.com",
            "https://link-artigo-gestao-pessoas-2.com",
            "https://link-video-gestao-pessoas.com",
            "https://link-artigo-gestao-pessoas-3.com",
            "https://link-video-gestao-pessoas-2.com"
        ],
        'estetica_avancada': [
            "https://link-artigo-estetica-1.com",
            "https://link-artigo-estetica-2.com",
            "https://link-video-estetica.com",
            "https://link-artigo-estetica-3.com",
            "https://link-video-estetica-2.com"
        ],
        'engenharia': [
            "https://link-artigo-engenharia-1.com",
            "https://link-artigo-engenharia-2.com",
            "https://link-video-engenharia.com",
            "https://link-artigo-engenharia-3.com",
            "https://link-video-engenharia-2.com"
        ],
        'arquitetura': [
            "https://link-artigo-arquitetura-1.com",
            "https://link-artigo-arquitetura-2.com",
            "https://link-video-arquitetura.com",
            "https://link-artigo-arquitetura-3.com",
            "https://link-video-arquitetura-2.com"
        ]
    }

    if trilha in links:
        texto = f"Aqui estão alguns links sobre {trilha.replace('_', ' ').capitalize()}:\n"
        for link in links[trilha]:
            texto += f"\n{link}"

        # Adicionar o botão de "Voltar ao Início"
        keyboard = [
            [InlineKeyboardButton("Voltar à Seleção de Trilhas", callback_data='voltar')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text=texto, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

    return 2

# Função de voltar à seleção de trilhas
async def voltar_ao_inicio(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Redireciona para a seleção das trilhas, sem enviar a mensagem de boas-vindas
    keyboard = [
        [InlineKeyboardButton("Marketing", callback_data='marketing')],
        [InlineKeyboardButton("Gestão de Pessoas", callback_data='gestao_pessoas')],
        [InlineKeyboardButton("Estética Avançada", callback_data='estetica_avancada')],
        [InlineKeyboardButton("Engenharia", callback_data='engenharia')],
        [InlineKeyboardButton("Arquitetura", callback_data='arquitetura')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    texto = "Escolha a trilha de conhecimento que você deseja explorar:"
    await query.edit_message_text(text=texto, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

    return 2

# Função principal para configurar o bot
def main() -> None:
    application = Application.builder().token("7856040500:AAH1GB3vO70iaFLv005mPl8I1xLWnSPXwz4").build()

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [CallbackQueryHandler(trilha, pattern='^iniciar$')],
            2: [CallbackQueryHandler(mostrar_links, pattern='^(marketing|gestao_pessoas|estetica_avancada|engenharia|arquitetura)$'),
                CallbackQueryHandler(voltar_ao_inicio, pattern='^voltar$')],
        },
        fallbacks=[],
    )

    application.add_handler(conversation_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
