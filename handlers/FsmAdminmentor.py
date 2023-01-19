from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from random import choice
from keyboards.client_kb import submit_markup, cancel_markup
from config import ADMINS


def id_gen():
    pers_id = ''
    while len(pers_id) != 5:
        id_items = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        new_id = choice(id_items)
        pers_id += new_id
    return pers_id


class FsmAdmin(StatesGroup):
    mentors_id = State()
    mentors_name = State()
    direction = State()
    mentors_age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.chat.id in ADMINS:
        await FsmAdmin.mentors_id.set()
        await message.answer(f" ID ментора сгенерирован! Хотите продолжить регестрацию?", reply_markup=submit_markup)
    else:
        await message.answer("Пиши в личку!")

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Cancled")


async def load_id(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        ment_id = id_gen()
        async with state.proxy() as data:
            data['mentors_id'] = ment_id
        await FsmAdmin.next()
        await message.answer("как зовут ментора?", reply_markup=cancel_markup)

    elif message.text.lower() == "нет":
        await state.finish()
    else:
        await message.answer("Нe понял!?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentors_name'] = message.text
    await FsmAdmin.next()
    await message.answer("направление мeнтора?", reply_markup=cancel_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FsmAdmin.next()
    await message.answer("сколько лет мeнтору?", reply_markup=cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) <= 0:
            await message.answer("Только положительные числа!")
        else:
            if 16 < int(message.text) < 50:
                async with state.proxy() as data:
                    data['mentors_age'] = message.text
                await FsmAdmin.next()
                await message.answer("c какой группы мeнтор?", reply_markup=cancel_markup)
            else:
                await message.answer("Доступ воспрещен!")
                await state.finish()
    except ValueError:
        await message.answer("Числа брат, числа")



async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FsmAdmin.next()
    await message.answer(f"Все ли правильно заполнено? ID: {data['mentors_id']} Name: {data['mentors_name']} "
                         f"Direction: {data['direction']} Age: {data['mentors_age']} "
                         f"Group: {data['group']} ", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await state.finish()
    elif message.text.lower() == "нет":
        await state.finish()
    else:
        await message.answer("Нe понял!?")


def register_handlers_mentors(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['CANCLE'])
    dp.register_message_handler(cancel_reg,
                                Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FsmAdmin.mentors_id)
    dp.register_message_handler(load_name, state=FsmAdmin.mentors_name)
    dp.register_message_handler(load_direction, state=FsmAdmin.direction)
    dp.register_message_handler(load_age, state=FsmAdmin.mentors_age)
    dp.register_message_handler(load_group, state=FsmAdmin.group)
    dp.register_message_handler(submit, state=FsmAdmin.submit)
