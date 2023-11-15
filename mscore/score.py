from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from mscore.db import get_db

bp = Blueprint('score', __name__)


@bp.route('/')
def index():
    db = get_db()
    games = db.execute(
        'SELECT game_id, game_name, player_count, date'
        ' FROM Games'
        ' ORDER BY date DESC'
    ).fetchall()
    return render_template('score/index.html', games=games)


@bp.route('/newgame-4p', methods=('GET', 'POST'))
def newgame_4p():
    if request.method == 'POST':
        player_count = 4
        game_name = request.form['game_name']
        initial_points = request.form['initial_points']
        return_points = request.form['return_points']
        score_to_money_conversion = request.form['score_to_money_conversion']
        chips_count = request.form['chips_count']
        uma_last_to_first = request.form['uma_last_to_first']
        uma_third_to_second = request.form['uma_third_to_second']
        tobi_penalty = request.form['tobi_penalty']
        error = None

        if not game_name:
            error = 'Game name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                'INSERT INTO Games (game_name, player_count, initial_points, return_points, score_to_money_conversion, chips_count, uma_last_to_first, uma_third_to_second, tobi_penalty)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (game_name, player_count, initial_points, return_points, score_to_money_conversion, chips_count,
                 uma_last_to_first, uma_third_to_second, tobi_penalty)
            )
            db.commit()

            # 追加されたデータのidを取得
            game_id = cursor.lastrowid
            cursor.close()
            return redirect(url_for('score.game', game_id=game_id))
    return render_template('score/newgame-4p.html')


@bp.route('/game/<int:game_id>/')
def game(game_id):
    db = get_db()
    game = db.execute(
        'SELECT game_id, game_name, player_count, date'
        ' FROM Games'
        ' WHERE game_id = ?',
        (game_id,)
    ).fetchone()

    if game is None:
        abort(404, f"Game id {game_id} doesn't exit.")

    return render_template('score/game.html', game=game)
