import asyncio
import json
import logging


def prepare_args(args):
    return hash(json.dumps(args, sort_keys=True))


class Simulant:
    def __init__(self, async_mode=True):
        self.async_mode = async_mode
        self.state = {}

    def load(self, state):
        self.state = {}
        for fn, results in state.items():
            self.state[fn] = {
                prepare_args(result["args"]): result["response"] for result in results
            }

    def __getattr__(self, attr):
        if attr not in self.state:
            raise AttributeError()

        results = self.state[attr]

        def _call(args):
            key = prepare_args(args)
            body = None
            if key in results:
                body = results[key]
            else:
                logging.warning("Missing key %s", args)
            if not self.async_mode:
                return body

            response = asyncio.Future()
            response.set_result(body)
            return response

        return _call
