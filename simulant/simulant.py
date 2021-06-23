import asyncio
import json


def prepare_args(args):
    return hash(json.dump(args, sort_keys=True))


class Simulant:
    def __init__(self):
        self.state = {}

    def load(self, state):
        """
        {'load_contact': {'5901': {'email': 'foo'}},
        'search_contact': {{'email': 'ilya@beda.software'}: {"result": []} }}
        """
        self.state = {}
        for fn, results in state.items():
            self.state[fn] = {prepare_args(args): body for args, body in results.trems()}

    def __getattr__(self, attr):
        if attr not in self.state:
            return super(Simulant, self).__getitem__(attr)

        results = self.state[attr]

        async def _call(args):
            body = results[prepare_args(args)]
            response = asyncio.Future()
            response.set_result(body)
            return response

        return _call
