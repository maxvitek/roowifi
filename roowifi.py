import requests
import json
import argparse
import argparse_actions


class Roomba(object):
    """
    This class abstracts a roowifi and gives attributes for telemetry data,
    as well as methods to command the robot
    """
    def __init__(self, ip, user='admin', passwd='roombawifi'):
        self.ip = ip
        self.user = user
        self.passwd = passwd
        self.auth = (self.user, self.passwd)

        try:
            self._telemetry = self.telemetry()
        except:
            raise Exception('Robot cannot be contacted at {%s}' % self.ip)

        self.charge = self._telemetry['response']['r18']['value']
        self.capacity = self._telemetry['response']['r19']['value']
        self.battery = 1. * self.charge / self.capacity

    def telemetry(self):
        """
        Roomba method which fetches telemetry data about the robot.  Returns
        a dictionary.
        """
        r = requests.get('http://' + self.ip + '/roomba.json', auth=self.auth)
        return json.loads(r.text)

    def clean(self):
        """
        Roomba method which commands the robot to emulate the 'clean' button press.  Returns
        requests response object.
        """
        r = requests.get('http://' + self.ip + '/rwr.cgi', params={'exec': '4'}, auth=self.auth)
        return r

    def spot(self):
        """
        Roomba method which commands the robot to emulate the 'spot clean' button press.  Returns
        requests response object.
        """
        r = requests.get('http://' + self.ip + '/rwr.cgi', params={'exec': '5'}, auth=self.auth)
        return r

    def dock(self):
        """
        Roomba method which commands the robot to emulate the 'dock' button press.  Returns
        requests response object.
        """
        r = requests.get('http://' + self.ip + '/rwr.cgi', params={'exec': '6'}, auth=self.auth)
        return r

    def idle(self):
        """
        Roomba method which commands the robot to idle.  Returns
        requests response object.
        """
        r = requests.get('http://' + self.ip + '/rwr.cgi', params={'exec': '1'}, auth=self.auth)
        return r


def main():
    parser = argparse.ArgumentParser(description='A commandline utility for controlling a Roomba via a RooWifi device.')
    parser.add_argument('ip_address', action=argparse_actions.ProperIpFormatAction, help='ip address of target robot')
    parser.add_argument('command', choices=('clean', 'spot', 'dock', 'idle'), help='command to be issued')
    parser.add_argument('-u', '--user', help='username')
    parser.add_argument('-p', '--passwd', help='password')

    try:
        args = parser.parse_args()
    except argparse_actions.InvalidIp as e:
        raise Exception('IP is invalid: {0}'.format(e.ip))

    kwargs = {}
    if args.user:
        kwargs['user'] = args.user
    if args.passwd:
        kwargs['passwd'] = args.passwd

    roomba = Roomba(args.ip_address, **kwargs)

    if args.command == 'clean':
        roomba.clean()
    elif args.command == 'spot':
        roomba.spot()
    elif args.command == 'dock':
        roomba.dock()
    elif args.command == 'idle':
        roomba.idle()

if __name__ == '__main__':
    main()
