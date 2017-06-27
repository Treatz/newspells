from evennia.commands.default.muxcommand import MuxCommand


class CmdLastBreath(MuxCommand):
   
    key = "+lastbreath"
    locks = "cmd:all()"

    def func(self):
        hit =  self.caller.search(self.args)
        self.caller.msg("The last person to attack him was %s." % hit.db.target)
