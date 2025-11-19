# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Data models for the Meta Game Environment.

The meta_game environment is a simple test environment that echoes back messages.
"""

from dataclasses import dataclass

from openenv_core.env_server.types import Action, Observation


@dataclass(kw_only=True)
class MetaGameAction(Action):
    """Actions your agent can perform."""

    move: str   # e.g., "up", "down", "left", "right"
    power: int = 1 # Optional parameter


@dataclass(kw_only=True)
class MetaGameObservation(Observation):
    """What your agent observes after each action."""
    score: int
    game_state: str
    is_game_over: bool = False

