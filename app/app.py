from flask import Flask, render_template, redirect, request

from base import BaseUnit, Arena
from classes import unit_classes
from equipment import Weapon, Armor, Equipment


app = Flask(__name__)

heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}

arena = Arena()  # инициализируем класс арены


@app.route("/")
def menu_page():
    # рендерим главное меню (шаблон index.html)
    return render_template('index.html')


@app.route("/fight/")
def start_fight():
    # TODO выполняем функцию start_game экземпляра класса арена и передаем ему необходимые аргументы
    # TODO рендерим экран боя (шаблон fight.html)
    pass

@app.route("/fight/hit")
def hit():
    # TODO кнопка нанесения удара
    # TODO обновляем экран боя (нанесение удара) (шаблон fight.html)
    # TODO если игра идет - вызываем метод player.hit() экземпляра класса арены
    # TODO если игра не идет - пропускаем срабатывание метода (простот рендерим шаблон с текущими данными)
    pass


@app.route("/fight/use-skill")
def use_skill():
    # TODO кнопка использования скилла
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    pass


@app.route("/fight/pass-turn")
def pass_turn():
    # TODO кнопка пропус хода
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    # TODO однако вызываем здесь функцию следующий ход (arena.next_turn())
    pass


@app.route("/fight/end-fight")
def end_fight():
    # TODO кнопка завершить игру - переход в главное меню
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    # TODO кнопка выбор героя. 2 метода GET и POST
    # TODO на GET отрисовываем форму.
    # TODO на POST отправляем форму и делаем редирект на эндпоинт choose enemy
    heroes_name = request.form.get('name')
    weapon = request.form.get("weapon")
    armor = request.form.get("armor")
    unit_class = request.form.get("unit_class")
    ar = arena.player(heroes_name, weapon, armor, unit_class)
    print(ar)

    header = 'Выбор героя'
    equipment = Equipment()
    weapons = equipment.get_weapons_names()
    armors = equipment.get_armors_names()
    classes = unit_classes
    return render_template('hero_choosing.html',
                           result={'header': header,
                                   "weapons": weapons,
                                   "armors": armors,
                                   "classes": classes})


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    # TODO кнопка выбор соперников. 2 метода GET и POST
    # TODO также на GET отрисовываем форму.
    # TODO а на POST отправляем форму и делаем редирект на начало битвы
    heroes_name = request.form.get('name')
    weapon = request.form.get("weapon")
    armor = request.form.get("armor")
    unit_class = request.form.get("unit_class")
    print(heroes_name, weapon, armor, unit_class)
    header = 'Выбор героя'
    equipment = Equipment()
    weapons = equipment.get_weapons_names()
    armors = equipment.get_armors_names()
    classes = unit_classes
    return render_template('hero_choosing.html',
                           result={'header': header,
                                   "weapons": weapons,
                                   "armors": armors,
                                   "classes": classes})


if __name__ == "__main__":
    app.run(debug=True, port=10000)
