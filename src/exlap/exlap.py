#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Tue Dec 20 01:06:12 2022 by generateDS.py version 2.41.1.
# Python 3.10.8 (main, Oct 13 2022, 09:48:40) [Clang 14.0.0 (clang-1400.0.29.102)]
#
# Command line options:
#   ('-f', '')
#   ('-s', 'schema/definitions.xsd')
#   ('-s', 'schema/object.xsd')
#   ('-s', 'schema/profile.xsd')
#   ('-o', 'exlap.py')
#
# Command line arguments:
#   schema/protocol.xsd
#
# Command line:
#   /opt/homebrew/bin/generateDS.py -f -s "schema/definitions.xsd" -s "schema/object.xsd" -s "schema/profile.xsd" -o "exlap.py" schema/protocol.xsd
#
# Current working directory (os.getcwd()):
#   EXLAP
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = ""
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': self.__class__.__name__,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            if sys.version_info.major == 2:
                from StringIO import StringIO
            else:
                from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % float(input_data)).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            input_data = input_data.strip()
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            target = str(target)
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

# from IPython.Shell import IPShellEmbed
# args = ''
# ipshell = IPShellEmbed(args,
#     banner = 'Dropping into IPython',
#     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    s1 = s1.replace('\n', '&#10;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class characteristicType(str, Enum):
    STATIC='static'
    DYNAMIC='dynamic'
    EVENT='event'


class commandSupportedType(str, Enum):
    SUPPORTED='supported'
    NOT_SUPPORTED='notSupported'


class contextType(str, Enum):
    GLOBAL='global'
    SESSION='session'


class phaseType(str, Enum):
    CHALLENGE='challenge'
    RESPONSE='response'


class portableType(str, Enum):
    U_8='u8'
    S_8='s8'
    U_16='u16'
    S_16='s16'
    U_32='u32'
    S_32='s32'
    U_64='u64'
    S_64='s64'
    STRING='string'
    FLOAT='float'
    DOUBLE='double'


class stateType(str, Enum):
    OK='ok'
    NODATA='nodata'
    ERROR='error'


class stateType3(str, Enum):
    OK='ok'
    NODATA='nodata'
    ERROR='error'


class statusType(str, Enum):
    OK='ok'
    ERROR='error'
    INTERNAL_ERROR='internalError'
    SYNTAX_ERROR='syntaxError'
    PROTOCOL_NOT_SUPPORTED='protocolNotSupported'
    NO_MATCHING_URL='noMatchingUrl'
    ACCESS_VIOLATION='accessViolation'
    SUBSCRIPTION_LIMIT_REACHED='subscriptionLimitReached'
    PROCESSING='processing'
    INVALID_PARAMETER='invalidParameter'
    NOT_IMPLEMENTED='notImplemented'
    AUTHENTICATION_FAILED='authenticationFailed'


class timeStampType(str, Enum):
    TRUE='true'
    FALSE='false'


class typeType(str, Enum):
    FUNCTION='function'
    OBJECT='object'


class Exlap(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Req=None, Status=None, Rsp=None, Dat=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Req is None:
            self.Req = []
        else:
            self.Req = Req
        self.Req_nsprefix_ = None
        if Status is None:
            self.Status = []
        else:
            self.Status = Status
        self.Status_nsprefix_ = None
        if Rsp is None:
            self.Rsp = []
        else:
            self.Rsp = Rsp
        self.Rsp_nsprefix_ = None
        if Dat is None:
            self.Dat = []
        else:
            self.Dat = Dat
        self.Dat_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Exlap)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Exlap.subclass:
            return Exlap.subclass(*args_, **kwargs_)
        else:
            return Exlap(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Req(self):
        return self.Req
    def set_Req(self, Req):
        self.Req = Req
    def add_Req(self, value):
        self.Req.append(value)
    def insert_Req_at(self, index, value):
        self.Req.insert(index, value)
    def replace_Req_at(self, index, value):
        self.Req[index] = value
    def get_Status(self):
        return self.Status
    def set_Status(self, Status):
        self.Status = Status
    def add_Status(self, value):
        self.Status.append(value)
    def insert_Status_at(self, index, value):
        self.Status.insert(index, value)
    def replace_Status_at(self, index, value):
        self.Status[index] = value
    def get_Rsp(self):
        return self.Rsp
    def set_Rsp(self, Rsp):
        self.Rsp = Rsp
    def add_Rsp(self, value):
        self.Rsp.append(value)
    def insert_Rsp_at(self, index, value):
        self.Rsp.insert(index, value)
    def replace_Rsp_at(self, index, value):
        self.Rsp[index] = value
    def get_Dat(self):
        return self.Dat
    def set_Dat(self, Dat):
        self.Dat = Dat
    def add_Dat(self, value):
        self.Dat.append(value)
    def insert_Dat_at(self, index, value):
        self.Dat.insert(index, value)
    def replace_Dat_at(self, index, value):
        self.Dat[index] = value
    def _hasContent(self):
        if (
            self.Req or
            self.Status or
            self.Rsp or
            self.Dat
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Exlap', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Exlap')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Exlap':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Exlap')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Exlap', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Exlap'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Exlap', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Req_ in self.Req:
            namespaceprefix_ = self.Req_nsprefix_ + ':' if (UseCapturedNS_ and self.Req_nsprefix_) else ''
            Req_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Req', pretty_print=pretty_print)
        for Status_ in self.Status:
            namespaceprefix_ = self.Status_nsprefix_ + ':' if (UseCapturedNS_ and self.Status_nsprefix_) else ''
            Status_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Status', pretty_print=pretty_print)
        for Rsp_ in self.Rsp:
            namespaceprefix_ = self.Rsp_nsprefix_ + ':' if (UseCapturedNS_ and self.Rsp_nsprefix_) else ''
            Rsp_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Rsp', pretty_print=pretty_print)
        for Dat_ in self.Dat:
            namespaceprefix_ = self.Dat_nsprefix_ + ':' if (UseCapturedNS_ and self.Dat_nsprefix_) else ''
            Dat_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Dat', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Req':
            obj_ = Req.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Req.append(obj_)
            obj_.original_tagname_ = 'Req'
        elif nodeName_ == 'Status':
            obj_ = Status.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Status.append(obj_)
            obj_.original_tagname_ = 'Status'
        elif nodeName_ == 'Rsp':
            obj_ = Rsp.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Rsp.append(obj_)
            obj_.original_tagname_ = 'Rsp'
        elif nodeName_ == 'Dat':
            obj_ = Dat.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Dat.append(obj_)
            obj_.original_tagname_ = 'Dat'
# end class Exlap


class Status(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, msg='', Init=None, Bye=None, Dataloss=None, Alive=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
        self.Init = Init
        self.Init_nsprefix_ = None
        self.Bye = Bye
        self.Bye_nsprefix_ = None
        self.Dataloss = Dataloss
        self.Dataloss_nsprefix_ = None
        self.Alive = Alive
        self.Alive_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Status)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Status.subclass:
            return Status.subclass(*args_, **kwargs_)
        else:
            return Status(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Init(self):
        return self.Init
    def set_Init(self, Init):
        self.Init = Init
    def get_Bye(self):
        return self.Bye
    def set_Bye(self, Bye):
        self.Bye = Bye
    def get_Dataloss(self):
        return self.Dataloss
    def set_Dataloss(self, Dataloss):
        self.Dataloss = Dataloss
    def get_Alive(self):
        return self.Alive
    def set_Alive(self, Alive):
        self.Alive = Alive
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def _hasContent(self):
        if (
            self.Init is not None or
            self.Bye is not None or
            self.Dataloss is not None or
            self.Alive is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Status', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Status')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Status':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Status')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Status', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Status'):
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Status', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Init is not None:
            namespaceprefix_ = self.Init_nsprefix_ + ':' if (UseCapturedNS_ and self.Init_nsprefix_) else ''
            self.Init.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Init', pretty_print=pretty_print)
        if self.Bye is not None:
            namespaceprefix_ = self.Bye_nsprefix_ + ':' if (UseCapturedNS_ and self.Bye_nsprefix_) else ''
            self.Bye.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Bye', pretty_print=pretty_print)
        if self.Dataloss is not None:
            namespaceprefix_ = self.Dataloss_nsprefix_ + ':' if (UseCapturedNS_ and self.Dataloss_nsprefix_) else ''
            self.Dataloss.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Dataloss', pretty_print=pretty_print)
        if self.Alive is not None:
            namespaceprefix_ = self.Alive_nsprefix_ + ':' if (UseCapturedNS_ and self.Alive_nsprefix_) else ''
            self.Alive.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alive', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Init':
            obj_ = InitType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Init = obj_
            obj_.original_tagname_ = 'Init'
        elif nodeName_ == 'Bye':
            obj_ = ByeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Bye = obj_
            obj_.original_tagname_ = 'Bye'
        elif nodeName_ == 'Dataloss':
            obj_ = DatalossType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Dataloss = obj_
            obj_.original_tagname_ = 'Dataloss'
        elif nodeName_ == 'Alive':
            obj_ = AliveType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alive = obj_
            obj_.original_tagname_ = 'Alive'
# end class Status


class Req(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id='0', Protocol=None, Dir=None, Subscribe=None, Unsubscribe=None, Call=None, Get=None, Bye=None, Alive=None, Heartbeat=None, Interface=None, Authenticate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        self.Protocol = Protocol
        self.Protocol_nsprefix_ = None
        self.Dir = Dir
        self.Dir_nsprefix_ = None
        self.Subscribe = Subscribe
        self.Subscribe_nsprefix_ = None
        self.Unsubscribe = Unsubscribe
        self.Unsubscribe_nsprefix_ = None
        self.Call = Call
        self.Call_nsprefix_ = None
        self.Get = Get
        self.Get_nsprefix_ = None
        self.Bye = Bye
        self.Bye_nsprefix_ = None
        self.Alive = Alive
        self.Alive_nsprefix_ = None
        self.Heartbeat = Heartbeat
        self.Heartbeat_nsprefix_ = None
        self.Interface = Interface
        self.Interface_nsprefix_ = None
        self.Authenticate = Authenticate
        self.Authenticate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Req)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Req.subclass:
            return Req.subclass(*args_, **kwargs_)
        else:
            return Req(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Protocol(self):
        return self.Protocol
    def set_Protocol(self, Protocol):
        self.Protocol = Protocol
    def get_Dir(self):
        return self.Dir
    def set_Dir(self, Dir):
        self.Dir = Dir
    def get_Subscribe(self):
        return self.Subscribe
    def set_Subscribe(self, Subscribe):
        self.Subscribe = Subscribe
    def get_Unsubscribe(self):
        return self.Unsubscribe
    def set_Unsubscribe(self, Unsubscribe):
        self.Unsubscribe = Unsubscribe
    def get_Call(self):
        return self.Call
    def set_Call(self, Call):
        self.Call = Call
    def get_Get(self):
        return self.Get
    def set_Get(self, Get):
        self.Get = Get
    def get_Bye(self):
        return self.Bye
    def set_Bye(self, Bye):
        self.Bye = Bye
    def get_Alive(self):
        return self.Alive
    def set_Alive(self, Alive):
        self.Alive = Alive
    def get_Heartbeat(self):
        return self.Heartbeat
    def set_Heartbeat(self, Heartbeat):
        self.Heartbeat = Heartbeat
    def get_Interface(self):
        return self.Interface
    def set_Interface(self, Interface):
        self.Interface = Interface
    def get_Authenticate(self):
        return self.Authenticate
    def set_Authenticate(self, Authenticate):
        self.Authenticate = Authenticate
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def validate_idType(self, value):
        # Validate type idType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on idType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 999999999:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on idType' % {"value": value, "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            self.Protocol is not None or
            self.Dir is not None or
            self.Subscribe is not None or
            self.Unsubscribe is not None or
            self.Call is not None or
            self.Get is not None or
            self.Bye is not None or
            self.Alive is not None or
            self.Heartbeat is not None or
            self.Interface is not None or
            self.Authenticate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Req', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Req')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Req':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Req')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Req', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Req'):
        if self.id != 0 and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id="%s"' % self.gds_format_integer(self.id, input_name='id'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Req', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Protocol is not None:
            namespaceprefix_ = self.Protocol_nsprefix_ + ':' if (UseCapturedNS_ and self.Protocol_nsprefix_) else ''
            self.Protocol.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Protocol', pretty_print=pretty_print)
        if self.Dir is not None:
            namespaceprefix_ = self.Dir_nsprefix_ + ':' if (UseCapturedNS_ and self.Dir_nsprefix_) else ''
            self.Dir.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Dir', pretty_print=pretty_print)
        if self.Subscribe is not None:
            namespaceprefix_ = self.Subscribe_nsprefix_ + ':' if (UseCapturedNS_ and self.Subscribe_nsprefix_) else ''
            self.Subscribe.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Subscribe', pretty_print=pretty_print)
        if self.Unsubscribe is not None:
            namespaceprefix_ = self.Unsubscribe_nsprefix_ + ':' if (UseCapturedNS_ and self.Unsubscribe_nsprefix_) else ''
            self.Unsubscribe.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Unsubscribe', pretty_print=pretty_print)
        if self.Call is not None:
            namespaceprefix_ = self.Call_nsprefix_ + ':' if (UseCapturedNS_ and self.Call_nsprefix_) else ''
            self.Call.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Call', pretty_print=pretty_print)
        if self.Get is not None:
            namespaceprefix_ = self.Get_nsprefix_ + ':' if (UseCapturedNS_ and self.Get_nsprefix_) else ''
            self.Get.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Get', pretty_print=pretty_print)
        if self.Bye is not None:
            namespaceprefix_ = self.Bye_nsprefix_ + ':' if (UseCapturedNS_ and self.Bye_nsprefix_) else ''
            self.Bye.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Bye', pretty_print=pretty_print)
        if self.Alive is not None:
            namespaceprefix_ = self.Alive_nsprefix_ + ':' if (UseCapturedNS_ and self.Alive_nsprefix_) else ''
            self.Alive.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alive', pretty_print=pretty_print)
        if self.Heartbeat is not None:
            namespaceprefix_ = self.Heartbeat_nsprefix_ + ':' if (UseCapturedNS_ and self.Heartbeat_nsprefix_) else ''
            self.Heartbeat.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Heartbeat', pretty_print=pretty_print)
        if self.Interface is not None:
            namespaceprefix_ = self.Interface_nsprefix_ + ':' if (UseCapturedNS_ and self.Interface_nsprefix_) else ''
            self.Interface.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Interface', pretty_print=pretty_print)
        if self.Authenticate is not None:
            namespaceprefix_ = self.Authenticate_nsprefix_ + ':' if (UseCapturedNS_ and self.Authenticate_nsprefix_) else ''
            self.Authenticate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Authenticate', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
            if self.id < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_idType(self.id)    # validate type idType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Protocol':
            obj_ = Protocol.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Protocol = obj_
            obj_.original_tagname_ = 'Protocol'
        elif nodeName_ == 'Dir':
            obj_ = Dir.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Dir = obj_
            obj_.original_tagname_ = 'Dir'
        elif nodeName_ == 'Subscribe':
            obj_ = Subscribe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Subscribe = obj_
            obj_.original_tagname_ = 'Subscribe'
        elif nodeName_ == 'Unsubscribe':
            obj_ = Unsubscribe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Unsubscribe = obj_
            obj_.original_tagname_ = 'Unsubscribe'
        elif nodeName_ == 'Call':
            obj_ = Call.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Call = obj_
            obj_.original_tagname_ = 'Call'
        elif nodeName_ == 'Get':
            obj_ = Get.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Get = obj_
            obj_.original_tagname_ = 'Get'
        elif nodeName_ == 'Bye':
            obj_ = Bye.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Bye = obj_
            obj_.original_tagname_ = 'Bye'
        elif nodeName_ == 'Alive':
            obj_ = Alive.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alive = obj_
            obj_.original_tagname_ = 'Alive'
        elif nodeName_ == 'Heartbeat':
            obj_ = Heartbeat.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Heartbeat = obj_
            obj_.original_tagname_ = 'Heartbeat'
        elif nodeName_ == 'Interface':
            obj_ = Interface.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Interface = obj_
            obj_.original_tagname_ = 'Interface'
        elif nodeName_ == 'Authenticate':
            obj_ = Authenticate.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Authenticate = obj_
            obj_.original_tagname_ = 'Authenticate'
# end class Req


class Interface(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Interface)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Interface.subclass:
            return Interface.subclass(*args_, **kwargs_)
        else:
            return Interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Interface', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Interface')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Interface':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Interface')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Interface', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Interface'):
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Interface', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Interface


class Protocol(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, version=None, returnCapabilities=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.version = _cast(int, version)
        self.version_nsprefix_ = None
        self.returnCapabilities = _cast(bool, returnCapabilities)
        self.returnCapabilities_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Protocol)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Protocol.subclass:
            return Protocol.subclass(*args_, **kwargs_)
        else:
            return Protocol(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_version(self):
        return self.version
    def set_version(self, version):
        self.version = version
    def get_returnCapabilities(self):
        return self.returnCapabilities
    def set_returnCapabilities(self, returnCapabilities):
        self.returnCapabilities = returnCapabilities
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Protocol', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Protocol')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Protocol':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Protocol')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Protocol', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Protocol'):
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            outfile.write(' version="%s"' % self.gds_format_integer(self.version, input_name='version'))
        if self.returnCapabilities and 'returnCapabilities' not in already_processed:
            already_processed.add('returnCapabilities')
            outfile.write(' returnCapabilities="%s"' % self.gds_format_boolean(self.returnCapabilities, input_name='returnCapabilities'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Protocol', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = self.gds_parse_integer(value, node, 'version')
            if self.version <= 0:
                raise_parse_error(node, 'Invalid PositiveInteger')
        value = find_attr_value_('returnCapabilities', node)
        if value is not None and 'returnCapabilities' not in already_processed:
            already_processed.add('returnCapabilities')
            if value in ('true', '1'):
                self.returnCapabilities = True
            elif value in ('false', '0'):
                self.returnCapabilities = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Protocol


class Get(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Get)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Get.subclass:
            return Get.subclass(*args_, **kwargs_)
        else:
            return Get(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Get', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Get')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Get':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Get')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Get', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Get'):
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Get', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Get


class Alive(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Alive)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Alive.subclass:
            return Alive.subclass(*args_, **kwargs_)
        else:
            return Alive(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Alive', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Alive')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Alive':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Alive')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Alive', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Alive'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Alive', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Alive


class Heartbeat(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ival=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ival = _cast(int, ival)
        self.ival_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Heartbeat)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Heartbeat.subclass:
            return Heartbeat.subclass(*args_, **kwargs_)
        else:
            return Heartbeat(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ival(self):
        return self.ival
    def set_ival(self, ival):
        self.ival = ival
    def validate_ivalType(self, value):
        # Validate type ivalType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on ivalType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on ivalType' % {"value": value, "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Heartbeat', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Heartbeat')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Heartbeat':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Heartbeat')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Heartbeat', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Heartbeat'):
        if self.ival is not None and 'ival' not in already_processed:
            already_processed.add('ival')
            outfile.write(' ival="%s"' % self.gds_format_integer(self.ival, input_name='ival'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Heartbeat', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ival', node)
        if value is not None and 'ival' not in already_processed:
            already_processed.add('ival')
            self.ival = self.gds_parse_integer(value, node, 'ival')
            if self.ival < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_ivalType(self.ival)    # validate type ivalType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Heartbeat


class Bye(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Bye)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Bye.subclass:
            return Bye.subclass(*args_, **kwargs_)
        else:
            return Bye(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Bye', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Bye')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Bye':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Bye')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Bye', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Bye'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Bye', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Bye


class Subscribe(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url=None, ival='0', content=True, timeStamp='false', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
        self.ival = _cast(int, ival)
        self.ival_nsprefix_ = None
        self.content = _cast(bool, content)
        self.content_nsprefix_ = None
        self.timeStamp = _cast(None, timeStamp)
        self.timeStamp_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Subscribe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Subscribe.subclass:
            return Subscribe.subclass(*args_, **kwargs_)
        else:
            return Subscribe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_ival(self):
        return self.ival
    def set_ival(self, ival):
        self.ival = ival
    def get_content(self):
        return self.content
    def set_content(self, content):
        self.content = content
    def get_timeStamp(self):
        return self.timeStamp
    def set_timeStamp(self, timeStamp):
        self.timeStamp = timeStamp
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_ivalType1(self, value):
        # Validate type ivalType1, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on ivalType1' % {"value": value, "lineno": lineno} )
                result = False
            if value > 60000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on ivalType1' % {"value": value, "lineno": lineno} )
                result = False
    def validate_timeStampType(self, value):
        # Validate type timeStampType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['true', 'false']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on timeStampType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Subscribe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Subscribe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Subscribe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Subscribe')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Subscribe', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Subscribe'):
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
        if self.ival != 0 and 'ival' not in already_processed:
            already_processed.add('ival')
            outfile.write(' ival="%s"' % self.gds_format_integer(self.ival, input_name='ival'))
        if not self.content and 'content' not in already_processed:
            already_processed.add('content')
            outfile.write(' content="%s"' % self.gds_format_boolean(self.content, input_name='content'))
        if self.timeStamp != "false" and 'timeStamp' not in already_processed:
            already_processed.add('timeStamp')
            outfile.write(' timeStamp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.timeStamp), input_name='timeStamp')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Subscribe', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
        value = find_attr_value_('ival', node)
        if value is not None and 'ival' not in already_processed:
            already_processed.add('ival')
            self.ival = self.gds_parse_integer(value, node, 'ival')
            if self.ival < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_ivalType1(self.ival)    # validate type ivalType1
        value = find_attr_value_('content', node)
        if value is not None and 'content' not in already_processed:
            already_processed.add('content')
            if value in ('true', '1'):
                self.content = True
            elif value in ('false', '0'):
                self.content = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('timeStamp', node)
        if value is not None and 'timeStamp' not in already_processed:
            already_processed.add('timeStamp')
            self.timeStamp = value
            self.timeStamp = ' '.join(self.timeStamp.split())
            self.validate_timeStampType(self.timeStamp)    # validate type timeStampType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Subscribe


class Authenticate(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, phase=None, user='', cnonce='', digest='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.phase = _cast(None, phase)
        self.phase_nsprefix_ = None
        self.user = _cast(None, user)
        self.user_nsprefix_ = None
        self.cnonce = _cast(None, cnonce)
        self.cnonce_nsprefix_ = None
        self.digest = _cast(None, digest)
        self.digest_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Authenticate)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Authenticate.subclass:
            return Authenticate.subclass(*args_, **kwargs_)
        else:
            return Authenticate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_phase(self):
        return self.phase
    def set_phase(self, phase):
        self.phase = phase
    def get_user(self):
        return self.user
    def set_user(self, user):
        self.user = user
    def get_cnonce(self):
        return self.cnonce
    def set_cnonce(self, cnonce):
        self.cnonce = cnonce
    def get_digest(self):
        return self.digest
    def set_digest(self, digest):
        self.digest = digest
    def validate_phaseType(self, value):
        # Validate type phaseType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['challenge', 'response']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on phaseType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Authenticate', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Authenticate')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Authenticate':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Authenticate')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Authenticate', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Authenticate'):
        if self.phase is not None and 'phase' not in already_processed:
            already_processed.add('phase')
            outfile.write(' phase=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.phase), input_name='phase')), ))
        if self.user != "" and 'user' not in already_processed:
            already_processed.add('user')
            outfile.write(' user=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.user), input_name='user')), ))
        if self.cnonce != "" and 'cnonce' not in already_processed:
            already_processed.add('cnonce')
            outfile.write(' cnonce=%s' % (quote_attrib(self.cnonce), ))
        if self.digest != "" and 'digest' not in already_processed:
            already_processed.add('digest')
            outfile.write(' digest=%s' % (quote_attrib(self.digest), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Authenticate', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('phase', node)
        if value is not None and 'phase' not in already_processed:
            already_processed.add('phase')
            self.phase = value
            self.phase = ' '.join(self.phase.split())
            self.validate_phaseType(self.phase)    # validate type phaseType
        value = find_attr_value_('user', node)
        if value is not None and 'user' not in already_processed:
            already_processed.add('user')
            self.user = value
        value = find_attr_value_('cnonce', node)
        if value is not None and 'cnonce' not in already_processed:
            already_processed.add('cnonce')
            self.cnonce = value
        value = find_attr_value_('digest', node)
        if value is not None and 'digest' not in already_processed:
            already_processed.add('digest')
            self.digest = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Authenticate


class Unsubscribe(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Unsubscribe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Unsubscribe.subclass:
            return Unsubscribe.subclass(*args_, **kwargs_)
        else:
            return Unsubscribe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Unsubscribe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Unsubscribe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Unsubscribe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Unsubscribe')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Unsubscribe', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Unsubscribe'):
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Unsubscribe', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Unsubscribe


class Dir(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, urlPattern='*', fromEntry=1, numOfEntries=999999999, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.urlPattern = _cast(None, urlPattern)
        self.urlPattern_nsprefix_ = None
        self.fromEntry = _cast(int, fromEntry)
        self.fromEntry_nsprefix_ = None
        self.numOfEntries = _cast(int, numOfEntries)
        self.numOfEntries_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Dir)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Dir.subclass:
            return Dir.subclass(*args_, **kwargs_)
        else:
            return Dir(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_urlPattern(self):
        return self.urlPattern
    def set_urlPattern(self, urlPattern):
        self.urlPattern = urlPattern
    def get_fromEntry(self):
        return self.fromEntry
    def set_fromEntry(self, fromEntry):
        self.fromEntry = fromEntry
    def get_numOfEntries(self):
        return self.numOfEntries
    def set_numOfEntries(self, numOfEntries):
        self.numOfEntries = numOfEntries
    def validate_urlPatternType(self, value):
        # Validate type urlPatternType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on urlPatternType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_urlPatternType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_urlPatternType_patterns_, ))
    validate_urlPatternType_patterns_ = [['^(\\*?[A-Za-z0-9_]*\\*?)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Dir', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Dir')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Dir':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Dir')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Dir', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Dir'):
        if self.urlPattern != "*" and 'urlPattern' not in already_processed:
            already_processed.add('urlPattern')
            outfile.write(' urlPattern=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.urlPattern), input_name='urlPattern')), ))
        if self.fromEntry != 1 and 'fromEntry' not in already_processed:
            already_processed.add('fromEntry')
            outfile.write(' fromEntry="%s"' % self.gds_format_integer(self.fromEntry, input_name='fromEntry'))
        if self.numOfEntries != 999999999 and 'numOfEntries' not in already_processed:
            already_processed.add('numOfEntries')
            outfile.write(' numOfEntries="%s"' % self.gds_format_integer(self.numOfEntries, input_name='numOfEntries'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Dir', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('urlPattern', node)
        if value is not None and 'urlPattern' not in already_processed:
            already_processed.add('urlPattern')
            self.urlPattern = value
            self.urlPattern = ' '.join(self.urlPattern.split())
            self.validate_urlPatternType(self.urlPattern)    # validate type urlPatternType
        value = find_attr_value_('fromEntry', node)
        if value is not None and 'fromEntry' not in already_processed:
            already_processed.add('fromEntry')
            self.fromEntry = self.gds_parse_integer(value, node, 'fromEntry')
            if self.fromEntry <= 0:
                raise_parse_error(node, 'Invalid PositiveInteger')
        value = find_attr_value_('numOfEntries', node)
        if value is not None and 'numOfEntries' not in already_processed:
            already_processed.add('numOfEntries')
            self.numOfEntries = self.gds_parse_integer(value, node, 'numOfEntries')
            if self.numOfEntries <= 0:
                raise_parse_error(node, 'Invalid PositiveInteger')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Dir


class Rsp(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id='0', status='ok', msg='', Type=None, Function=None, Object=None, ObjectData=None, UrlList=None, Result=None, Challenge=None, Capabilities=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        self.status = _cast(None, status)
        self.status_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
        self.Type = Type
        self.Type_nsprefix_ = None
        self.Function = Function
        self.Function_nsprefix_ = None
        self.Object = Object
        self.Object_nsprefix_ = None
        self.ObjectData = ObjectData
        self.ObjectData_nsprefix_ = None
        self.UrlList = UrlList
        self.UrlList_nsprefix_ = None
        self.Result = Result
        self.Result_nsprefix_ = None
        self.Challenge = Challenge
        self.Challenge_nsprefix_ = None
        self.Capabilities = Capabilities
        self.Capabilities_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Rsp)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Rsp.subclass:
            return Rsp.subclass(*args_, **kwargs_)
        else:
            return Rsp(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def get_Function(self):
        return self.Function
    def set_Function(self, Function):
        self.Function = Function
    def get_Object(self):
        return self.Object
    def set_Object(self, Object):
        self.Object = Object
    def get_ObjectData(self):
        return self.ObjectData
    def set_ObjectData(self, ObjectData):
        self.ObjectData = ObjectData
    def get_UrlList(self):
        return self.UrlList
    def set_UrlList(self, UrlList):
        self.UrlList = UrlList
    def get_Result(self):
        return self.Result
    def set_Result(self, Result):
        self.Result = Result
    def get_Challenge(self):
        return self.Challenge
    def set_Challenge(self, Challenge):
        self.Challenge = Challenge
    def get_Capabilities(self):
        return self.Capabilities
    def set_Capabilities(self, Capabilities):
        self.Capabilities = Capabilities
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_idType2(self, value):
        # Validate type idType2, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on idType2' % {"value": value, "lineno": lineno} )
                result = False
            if value > 999999999:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on idType2' % {"value": value, "lineno": lineno} )
                result = False
    def validate_statusType(self, value):
        # Validate type statusType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'error', 'internalError', 'syntaxError', 'protocolNotSupported', 'noMatchingUrl', 'accessViolation', 'subscriptionLimitReached', 'processing', 'invalidParameter', 'notImplemented', 'authenticationFailed']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on statusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            self.Type is not None or
            self.Function is not None or
            self.Object is not None or
            self.ObjectData is not None or
            self.UrlList is not None or
            self.Result is not None or
            self.Challenge is not None or
            self.Capabilities is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Rsp', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Rsp')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Rsp':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Rsp')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Rsp', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Rsp'):
        if self.id != 0 and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id="%s"' % self.gds_format_integer(self.id, input_name='id'))
        if self.status != "ok" and 'status' not in already_processed:
            already_processed.add('status')
            outfile.write(' status=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.status), input_name='status')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Rsp', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            namespaceprefix_ = self.Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Type_nsprefix_) else ''
            self.Type.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Type', pretty_print=pretty_print)
        if self.Function is not None:
            namespaceprefix_ = self.Function_nsprefix_ + ':' if (UseCapturedNS_ and self.Function_nsprefix_) else ''
            self.Function.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Function', pretty_print=pretty_print)
        if self.Object is not None:
            namespaceprefix_ = self.Object_nsprefix_ + ':' if (UseCapturedNS_ and self.Object_nsprefix_) else ''
            self.Object.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Object', pretty_print=pretty_print)
        if self.ObjectData is not None:
            namespaceprefix_ = self.ObjectData_nsprefix_ + ':' if (UseCapturedNS_ and self.ObjectData_nsprefix_) else ''
            self.ObjectData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ObjectData', pretty_print=pretty_print)
        if self.UrlList is not None:
            namespaceprefix_ = self.UrlList_nsprefix_ + ':' if (UseCapturedNS_ and self.UrlList_nsprefix_) else ''
            self.UrlList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UrlList', pretty_print=pretty_print)
        if self.Result is not None:
            namespaceprefix_ = self.Result_nsprefix_ + ':' if (UseCapturedNS_ and self.Result_nsprefix_) else ''
            self.Result.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Result', pretty_print=pretty_print)
        if self.Challenge is not None:
            namespaceprefix_ = self.Challenge_nsprefix_ + ':' if (UseCapturedNS_ and self.Challenge_nsprefix_) else ''
            self.Challenge.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Challenge', pretty_print=pretty_print)
        if self.Capabilities is not None:
            namespaceprefix_ = self.Capabilities_nsprefix_ + ':' if (UseCapturedNS_ and self.Capabilities_nsprefix_) else ''
            self.Capabilities.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Capabilities', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
            if self.id < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_idType2(self.id)    # validate type idType2
        value = find_attr_value_('status', node)
        if value is not None and 'status' not in already_processed:
            already_processed.add('status')
            self.status = value
            self.status = ' '.join(self.status.split())
            self.validate_statusType(self.status)    # validate type statusType
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Type':
            obj_ = Type.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Type = obj_
            obj_.original_tagname_ = 'Type'
        elif nodeName_ == 'Function':
            obj_ = Function.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Function = obj_
            obj_.original_tagname_ = 'Function'
        elif nodeName_ == 'Object':
            obj_ = Object.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Object = obj_
            obj_.original_tagname_ = 'Object'
        elif nodeName_ == 'ObjectData':
            obj_ = ObjectData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ObjectData = obj_
            obj_.original_tagname_ = 'ObjectData'
        elif nodeName_ == 'UrlList':
            obj_ = UrlList.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UrlList = obj_
            obj_.original_tagname_ = 'UrlList'
        elif nodeName_ == 'Result':
            obj_ = Result.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Result = obj_
            obj_.original_tagname_ = 'Result'
        elif nodeName_ == 'Challenge':
            obj_ = Challenge.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Challenge = obj_
            obj_.original_tagname_ = 'Challenge'
        elif nodeName_ == 'Capabilities':
            obj_ = Capabilities.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Capabilities = obj_
            obj_.original_tagname_ = 'Capabilities'
# end class Rsp


class Capabilities(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service=None, description='', version='1.0', Supports=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.service = _cast(None, service)
        self.service_nsprefix_ = None
        self.description = _cast(None, description)
        self.description_nsprefix_ = None
        self.version = _cast(None, version)
        self.version_nsprefix_ = None
        self.Supports = Supports
        self.Supports_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Capabilities)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Capabilities.subclass:
            return Capabilities.subclass(*args_, **kwargs_)
        else:
            return Capabilities(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Supports(self):
        return self.Supports
    def set_Supports(self, Supports):
        self.Supports = Supports
    def get_service(self):
        return self.service
    def set_service(self, service):
        self.service = service
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_version(self):
        return self.version
    def set_version(self, version):
        self.version = version
    def validate_versionType(self, value):
        # Validate type versionType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on versionType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_versionType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_versionType_patterns_, ))
    validate_versionType_patterns_ = [['^([1-9].[0-9])$']]
    def _hasContent(self):
        if (
            self.Supports is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Capabilities', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Capabilities')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Capabilities':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Capabilities')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Capabilities', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Capabilities'):
        if self.service is not None and 'service' not in already_processed:
            already_processed.add('service')
            outfile.write(' service=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.service), input_name='service')), ))
        if self.description != "" and 'description' not in already_processed:
            already_processed.add('description')
            outfile.write(' description=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.description), input_name='description')), ))
        if self.version != "1.0" and 'version' not in already_processed:
            already_processed.add('version')
            outfile.write(' version=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.version), input_name='version')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Capabilities', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Supports is not None:
            namespaceprefix_ = self.Supports_nsprefix_ + ':' if (UseCapturedNS_ and self.Supports_nsprefix_) else ''
            self.Supports.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Supports', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('service', node)
        if value is not None and 'service' not in already_processed:
            already_processed.add('service')
            self.service = value
        value = find_attr_value_('description', node)
        if value is not None and 'description' not in already_processed:
            already_processed.add('description')
            self.description = value
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
            self.version = ' '.join(self.version.split())
            self.validate_versionType(self.version)    # validate type versionType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Supports':
            obj_ = Supports.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Supports = obj_
            obj_.original_tagname_ = 'Supports'
# end class Capabilities


class Supports(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, protocol=None, interface=False, authenticate=False, heartbeat=False, datTimeStamp=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.protocol = _cast(None, protocol)
        self.protocol_nsprefix_ = None
        self.interface = _cast(bool, interface)
        self.interface_nsprefix_ = None
        self.authenticate = _cast(bool, authenticate)
        self.authenticate_nsprefix_ = None
        self.heartbeat = _cast(bool, heartbeat)
        self.heartbeat_nsprefix_ = None
        self.datTimeStamp = _cast(bool, datTimeStamp)
        self.datTimeStamp_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Supports)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Supports.subclass:
            return Supports.subclass(*args_, **kwargs_)
        else:
            return Supports(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_protocol(self):
        return self.protocol
    def set_protocol(self, protocol):
        self.protocol = protocol
    def get_interface(self):
        return self.interface
    def set_interface(self, interface):
        self.interface = interface
    def get_authenticate(self):
        return self.authenticate
    def set_authenticate(self, authenticate):
        self.authenticate = authenticate
    def get_heartbeat(self):
        return self.heartbeat
    def set_heartbeat(self, heartbeat):
        self.heartbeat = heartbeat
    def get_datTimeStamp(self):
        return self.datTimeStamp
    def set_datTimeStamp(self, datTimeStamp):
        self.datTimeStamp = datTimeStamp
    def validate_protocolType(self, value):
        # Validate type protocolType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on protocolType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_protocolType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_protocolType_patterns_, ))
    validate_protocolType_patterns_ = [['^([0-9].[0-9])$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Supports', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Supports')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Supports':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Supports')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Supports', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Supports'):
        if self.protocol is not None and 'protocol' not in already_processed:
            already_processed.add('protocol')
            outfile.write(' protocol=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.protocol), input_name='protocol')), ))
        if self.interface and 'interface' not in already_processed:
            already_processed.add('interface')
            outfile.write(' interface="%s"' % self.gds_format_boolean(self.interface, input_name='interface'))
        if self.authenticate and 'authenticate' not in already_processed:
            already_processed.add('authenticate')
            outfile.write(' authenticate="%s"' % self.gds_format_boolean(self.authenticate, input_name='authenticate'))
        if self.heartbeat and 'heartbeat' not in already_processed:
            already_processed.add('heartbeat')
            outfile.write(' heartbeat="%s"' % self.gds_format_boolean(self.heartbeat, input_name='heartbeat'))
        if self.datTimeStamp and 'datTimeStamp' not in already_processed:
            already_processed.add('datTimeStamp')
            outfile.write(' datTimeStamp="%s"' % self.gds_format_boolean(self.datTimeStamp, input_name='datTimeStamp'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Supports', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('protocol', node)
        if value is not None and 'protocol' not in already_processed:
            already_processed.add('protocol')
            self.protocol = value
            self.protocol = ' '.join(self.protocol.split())
            self.validate_protocolType(self.protocol)    # validate type protocolType
        value = find_attr_value_('interface', node)
        if value is not None and 'interface' not in already_processed:
            already_processed.add('interface')
            if value in ('true', '1'):
                self.interface = True
            elif value in ('false', '0'):
                self.interface = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('authenticate', node)
        if value is not None and 'authenticate' not in already_processed:
            already_processed.add('authenticate')
            if value in ('true', '1'):
                self.authenticate = True
            elif value in ('false', '0'):
                self.authenticate = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('heartbeat', node)
        if value is not None and 'heartbeat' not in already_processed:
            already_processed.add('heartbeat')
            if value in ('true', '1'):
                self.heartbeat = True
            elif value in ('false', '0'):
                self.heartbeat = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('datTimeStamp', node)
        if value is not None and 'datTimeStamp' not in already_processed:
            already_processed.add('datTimeStamp')
            if value in ('true', '1'):
                self.datTimeStamp = True
            elif value in ('false', '0'):
                self.datTimeStamp = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Supports


class Challenge(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, nonce='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.nonce = _cast(None, nonce)
        self.nonce_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Challenge)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Challenge.subclass:
            return Challenge.subclass(*args_, **kwargs_)
        else:
            return Challenge(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_nonce(self):
        return self.nonce
    def set_nonce(self, nonce):
        self.nonce = nonce
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Challenge', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Challenge')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Challenge':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Challenge')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Challenge', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Challenge'):
        if self.nonce != "" and 'nonce' not in already_processed:
            already_processed.add('nonce')
            outfile.write(' nonce=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.nonce), input_name='nonce')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Challenge', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('nonce', node)
        if value is not None and 'nonce' not in already_processed:
            already_processed.add('nonce')
            self.nonce = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Challenge


class UrlList(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Match=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Match is None:
            self.Match = []
        else:
            self.Match = Match
        self.Match_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UrlList)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UrlList.subclass:
            return UrlList.subclass(*args_, **kwargs_)
        else:
            return UrlList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Match(self):
        return self.Match
    def set_Match(self, Match):
        self.Match = Match
    def add_Match(self, value):
        self.Match.append(value)
    def insert_Match_at(self, index, value):
        self.Match.insert(index, value)
    def replace_Match_at(self, index, value):
        self.Match[index] = value
    def _hasContent(self):
        if (
            self.Match
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='UrlList', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UrlList')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UrlList':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UrlList')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UrlList', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UrlList'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='UrlList', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Match_ in self.Match:
            namespaceprefix_ = self.Match_nsprefix_ + ':' if (UseCapturedNS_ and self.Match_nsprefix_) else ''
            Match_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Match', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Match':
            obj_ = Match.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Match.append(obj_)
            obj_.original_tagname_ = 'Match'
# end class UrlList


class Match(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url=None, type_='object', isSubscribed=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.isSubscribed = _cast(bool, isSubscribed)
        self.isSubscribed_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Match)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Match.subclass:
            return Match.subclass(*args_, **kwargs_)
        else:
            return Match(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_isSubscribed(self):
        return self.isSubscribed
    def set_isSubscribed(self, isSubscribed):
        self.isSubscribed = isSubscribed
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_typeType(self, value):
        # Validate type typeType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['function', 'object']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on typeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Match', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Match')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Match':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Match')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Match', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Match'):
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
        if self.type_ != "object" and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.isSubscribed and 'isSubscribed' not in already_processed:
            already_processed.add('isSubscribed')
            outfile.write(' isSubscribed="%s"' % self.gds_format_boolean(self.isSubscribed, input_name='isSubscribed'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Match', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.type_ = ' '.join(self.type_.split())
            self.validate_typeType(self.type_)    # validate type typeType
        value = find_attr_value_('isSubscribed', node)
        if value is not None and 'isSubscribed' not in already_processed:
            already_processed.add('isSubscribed')
            if value in ('true', '1'):
                self.isSubscribed = True
            elif value in ('false', '0'):
                self.isSubscribed = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Match


class baseValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, baseValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if baseValueType.subclass:
            return baseValueType.subclass(*args_, **kwargs_)
        else:
            return baseValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType(self, value):
        # Validate type stateType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='baseValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('baseValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'baseValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='baseValueType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='baseValueType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='baseValueType'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='baseValueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType(self.state)    # validate type stateType
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class baseValueType


class Abs(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, val=0, name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.val = _cast(float, val)
        self.val_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Abs)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Abs.subclass:
            return Abs.subclass(*args_, **kwargs_)
        else:
            return Abs(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_val(self):
        return self.val
    def set_val(self, val):
        self.val = val
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Abs', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Abs')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Abs':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Abs')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Abs', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Abs'):
        if self.val != 0 and 'val' not in already_processed:
            already_processed.add('val')
            outfile.write(' val="%s"' % self.gds_format_double(self.val, input_name='val'))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Abs', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('val', node)
        if value is not None and 'val' not in already_processed:
            already_processed.add('val')
            value = self.gds_parse_double(value, node, 'val')
            self.val = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Abs


class Act(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, val=False, name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.val = _cast(bool, val)
        self.val_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Act)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Act.subclass:
            return Act.subclass(*args_, **kwargs_)
        else:
            return Act(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_val(self):
        return self.val
    def set_val(self, val):
        self.val = val
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Act', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Act')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Act':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Act')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Act', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Act'):
        if self.val and 'val' not in already_processed:
            already_processed.add('val')
            outfile.write(' val="%s"' % self.gds_format_boolean(self.val, input_name='val'))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Act', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('val', node)
        if value is not None and 'val' not in already_processed:
            already_processed.add('val')
            if value in ('true', '1'):
                self.val = True
            elif value in ('false', '0'):
                self.val = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Act


class Bin(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, val='', name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.val = _cast(None, val)
        self.val_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Bin)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Bin.subclass:
            return Bin.subclass(*args_, **kwargs_)
        else:
            return Bin(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_val(self):
        return self.val
    def set_val(self, val):
        self.val = val
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Bin', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Bin')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Bin':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Bin')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Bin', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Bin'):
        if self.val != "" and 'val' not in already_processed:
            already_processed.add('val')
            outfile.write(' val=%s' % (quote_attrib(self.val), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Bin', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('val', node)
        if value is not None and 'val' not in already_processed:
            already_processed.add('val')
            self.val = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Bin


class Enm(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, val='default', name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.val = _cast(None, val)
        self.val_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Enm)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Enm.subclass:
            return Enm.subclass(*args_, **kwargs_)
        else:
            return Enm(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_val(self):
        return self.val
    def set_val(self, val):
        self.val = val
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_identifierType(self, value):
        # Validate type identifierType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on identifierType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on identifierType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_identifierType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_identifierType_patterns_, ))
    validate_identifierType_patterns_ = [['^([A-Za-z0-9_]+)$']]
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Enm', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Enm')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Enm':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Enm')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Enm', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Enm'):
        if self.val != "default" and 'val' not in already_processed:
            already_processed.add('val')
            outfile.write(' val=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.val), input_name='val')), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Enm', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('val', node)
        if value is not None and 'val' not in already_processed:
            already_processed.add('val')
            self.val = value
            self.val = ' '.join(self.val.split())
            self.validate_identifierType(self.val)    # validate type identifierType
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Enm


class Txt(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, val='', name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.val = _cast(None, val)
        self.val_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Txt)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Txt.subclass:
            return Txt.subclass(*args_, **kwargs_)
        else:
            return Txt(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_val(self):
        return self.val
    def set_val(self, val):
        self.val = val
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Txt', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Txt')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Txt':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Txt')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Txt', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Txt'):
        if self.val != "" and 'val' not in already_processed:
            already_processed.add('val')
            outfile.write(' val=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.val), input_name='val')), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Txt', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('val', node)
        if value is not None and 'val' not in already_processed:
            already_processed.add('val')
            self.val = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Txt


class Rel(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, val=0, name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.val = _cast(float, val)
        self.val_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Rel)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Rel.subclass:
            return Rel.subclass(*args_, **kwargs_)
        else:
            return Rel(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_val(self):
        return self.val
    def set_val(self, val):
        self.val = val
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Rel', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Rel')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Rel':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Rel')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Rel', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Rel'):
        if self.val != 0 and 'val' not in already_processed:
            already_processed.add('val')
            outfile.write(' val="%s"' % self.gds_format_double(self.val, input_name='val'))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Rel', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('val', node)
        if value is not None and 'val' not in already_processed:
            already_processed.add('val')
            value = self.gds_parse_double(value, node, 'val')
            self.val = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Rel


class Tim(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, val='1970-01-01T00:00:00.000Z', name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.val = _cast(None, val)
        self.val_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Tim)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Tim.subclass:
            return Tim.subclass(*args_, **kwargs_)
        else:
            return Tim(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_val(self):
        return self.val
    def set_val(self, val):
        self.val = val
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_valType(self, value):
        # Validate type valType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_valType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_valType_patterns_, ))
    validate_valType_patterns_ = [['^([0-9]{4}-[0-2][0-9]-[0-3][0-9]T[0-2][0-9](:[0-5][0-9]){2}(\\.[0-9]{1,6})?(Z|(\\+|-)[0-9]{2}:[0-9]{2})|[0-9]{4}-[0-2][0-9]-[0-3][0-9]|[0-2][0-9](:[0-5][0-9]){2}(\\.[0-9]{1,6})?(Z|(\\+|-)[0-9]{2}:[0-9]{2}))$']]
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Tim', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Tim')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Tim':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Tim')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Tim', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Tim'):
        if self.val != "1970-01-01T00:00:00.000Z" and 'val' not in already_processed:
            already_processed.add('val')
            outfile.write(' val=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.val), input_name='val')), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Tim', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('val', node)
        if value is not None and 'val' not in already_processed:
            already_processed.add('val')
            self.val = value
            self.validate_valType(self.val)    # validate type valType
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Tim


class List(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, state='ok', msg='', Elem=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
        if Elem is None:
            self.Elem = []
        else:
            self.Elem = Elem
        self.Elem_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, List)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if List.subclass:
            return List.subclass(*args_, **kwargs_)
        else:
            return List(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Elem(self):
        return self.Elem
    def set_Elem(self, Elem):
        self.Elem = Elem
    def add_Elem(self, value):
        self.Elem.append(value)
    def insert_Elem_at(self, index, value):
        self.Elem.insert(index, value)
    def replace_Elem_at(self, index, value):
        self.Elem[index] = value
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            self.Elem
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='List', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('List')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'List':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='List')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='List', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='List'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='List', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Elem_ in self.Elem:
            namespaceprefix_ = self.Elem_nsprefix_ + ':' if (UseCapturedNS_ and self.Elem_nsprefix_) else ''
            Elem_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Elem', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Elem':
            obj_ = Elem.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Elem.append(obj_)
            obj_.original_tagname_ = 'Elem'
# end class List


class basicElements(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Abs is None:
            self.Abs = []
        else:
            self.Abs = Abs
        self.Abs_nsprefix_ = None
        if Act is None:
            self.Act = []
        else:
            self.Act = Act
        self.Act_nsprefix_ = None
        if Alt is None:
            self.Alt = []
        else:
            self.Alt = Alt
        self.Alt_nsprefix_ = None
        if Bin is None:
            self.Bin = []
        else:
            self.Bin = Bin
        self.Bin_nsprefix_ = None
        if Enm is None:
            self.Enm = []
        else:
            self.Enm = Enm
        self.Enm_nsprefix_ = None
        if Txt is None:
            self.Txt = []
        else:
            self.Txt = Txt
        self.Txt_nsprefix_ = None
        if Rel is None:
            self.Rel = []
        else:
            self.Rel = Rel
        self.Rel_nsprefix_ = None
        if Tim is None:
            self.Tim = []
        else:
            self.Tim = Tim
        self.Tim_nsprefix_ = None
        if List is None:
            self.List = []
        else:
            self.List = List
        self.List_nsprefix_ = None
        if Obj is None:
            self.Obj = []
        else:
            self.Obj = Obj
        self.Obj_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, basicElements)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if basicElements.subclass:
            return basicElements.subclass(*args_, **kwargs_)
        else:
            return basicElements(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Abs(self):
        return self.Abs
    def set_Abs(self, Abs):
        self.Abs = Abs
    def add_Abs(self, value):
        self.Abs.append(value)
    def insert_Abs_at(self, index, value):
        self.Abs.insert(index, value)
    def replace_Abs_at(self, index, value):
        self.Abs[index] = value
    def get_Act(self):
        return self.Act
    def set_Act(self, Act):
        self.Act = Act
    def add_Act(self, value):
        self.Act.append(value)
    def insert_Act_at(self, index, value):
        self.Act.insert(index, value)
    def replace_Act_at(self, index, value):
        self.Act[index] = value
    def get_Alt(self):
        return self.Alt
    def set_Alt(self, Alt):
        self.Alt = Alt
    def add_Alt(self, value):
        self.Alt.append(value)
    def insert_Alt_at(self, index, value):
        self.Alt.insert(index, value)
    def replace_Alt_at(self, index, value):
        self.Alt[index] = value
    def get_Bin(self):
        return self.Bin
    def set_Bin(self, Bin):
        self.Bin = Bin
    def add_Bin(self, value):
        self.Bin.append(value)
    def insert_Bin_at(self, index, value):
        self.Bin.insert(index, value)
    def replace_Bin_at(self, index, value):
        self.Bin[index] = value
    def get_Enm(self):
        return self.Enm
    def set_Enm(self, Enm):
        self.Enm = Enm
    def add_Enm(self, value):
        self.Enm.append(value)
    def insert_Enm_at(self, index, value):
        self.Enm.insert(index, value)
    def replace_Enm_at(self, index, value):
        self.Enm[index] = value
    def get_Txt(self):
        return self.Txt
    def set_Txt(self, Txt):
        self.Txt = Txt
    def add_Txt(self, value):
        self.Txt.append(value)
    def insert_Txt_at(self, index, value):
        self.Txt.insert(index, value)
    def replace_Txt_at(self, index, value):
        self.Txt[index] = value
    def get_Rel(self):
        return self.Rel
    def set_Rel(self, Rel):
        self.Rel = Rel
    def add_Rel(self, value):
        self.Rel.append(value)
    def insert_Rel_at(self, index, value):
        self.Rel.insert(index, value)
    def replace_Rel_at(self, index, value):
        self.Rel[index] = value
    def get_Tim(self):
        return self.Tim
    def set_Tim(self, Tim):
        self.Tim = Tim
    def add_Tim(self, value):
        self.Tim.append(value)
    def insert_Tim_at(self, index, value):
        self.Tim.insert(index, value)
    def replace_Tim_at(self, index, value):
        self.Tim[index] = value
    def get_List(self):
        return self.List
    def set_List(self, List):
        self.List = List
    def add_List(self, value):
        self.List.append(value)
    def insert_List_at(self, index, value):
        self.List.insert(index, value)
    def replace_List_at(self, index, value):
        self.List[index] = value
    def get_Obj(self):
        return self.Obj
    def set_Obj(self, Obj):
        self.Obj = Obj
    def add_Obj(self, value):
        self.Obj.append(value)
    def insert_Obj_at(self, index, value):
        self.Obj.insert(index, value)
    def replace_Obj_at(self, index, value):
        self.Obj[index] = value
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.Abs or
            self.Act or
            self.Alt or
            self.Bin or
            self.Enm or
            self.Txt or
            self.Rel or
            self.Tim or
            self.List or
            self.Obj
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='basicElements', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('basicElements')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'basicElements':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='basicElements')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='basicElements', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='basicElements'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='basicElements', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Abs_ in self.Abs:
            namespaceprefix_ = self.Abs_nsprefix_ + ':' if (UseCapturedNS_ and self.Abs_nsprefix_) else ''
            Abs_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Abs', pretty_print=pretty_print)
        for Act_ in self.Act:
            namespaceprefix_ = self.Act_nsprefix_ + ':' if (UseCapturedNS_ and self.Act_nsprefix_) else ''
            Act_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Act', pretty_print=pretty_print)
        for Alt_ in self.Alt:
            namespaceprefix_ = self.Alt_nsprefix_ + ':' if (UseCapturedNS_ and self.Alt_nsprefix_) else ''
            Alt_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alt', pretty_print=pretty_print)
        for Bin_ in self.Bin:
            namespaceprefix_ = self.Bin_nsprefix_ + ':' if (UseCapturedNS_ and self.Bin_nsprefix_) else ''
            Bin_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Bin', pretty_print=pretty_print)
        for Enm_ in self.Enm:
            namespaceprefix_ = self.Enm_nsprefix_ + ':' if (UseCapturedNS_ and self.Enm_nsprefix_) else ''
            Enm_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Enm', pretty_print=pretty_print)
        for Txt_ in self.Txt:
            namespaceprefix_ = self.Txt_nsprefix_ + ':' if (UseCapturedNS_ and self.Txt_nsprefix_) else ''
            Txt_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Txt', pretty_print=pretty_print)
        for Rel_ in self.Rel:
            namespaceprefix_ = self.Rel_nsprefix_ + ':' if (UseCapturedNS_ and self.Rel_nsprefix_) else ''
            Rel_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Rel', pretty_print=pretty_print)
        for Tim_ in self.Tim:
            namespaceprefix_ = self.Tim_nsprefix_ + ':' if (UseCapturedNS_ and self.Tim_nsprefix_) else ''
            Tim_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Tim', pretty_print=pretty_print)
        for List_ in self.List:
            namespaceprefix_ = self.List_nsprefix_ + ':' if (UseCapturedNS_ and self.List_nsprefix_) else ''
            List_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='List', pretty_print=pretty_print)
        for Obj_ in self.Obj:
            namespaceprefix_ = self.Obj_nsprefix_ + ':' if (UseCapturedNS_ and self.Obj_nsprefix_) else ''
            Obj_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Obj', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Abs':
            obj_ = Abs.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Abs.append(obj_)
            obj_.original_tagname_ = 'Abs'
        elif nodeName_ == 'Act':
            obj_ = Act.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Act.append(obj_)
            obj_.original_tagname_ = 'Act'
        elif nodeName_ == 'Alt':
            obj_ = Alt.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alt.append(obj_)
            obj_.original_tagname_ = 'Alt'
        elif nodeName_ == 'Bin':
            obj_ = Bin.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Bin.append(obj_)
            obj_.original_tagname_ = 'Bin'
        elif nodeName_ == 'Enm':
            obj_ = Enm.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Enm.append(obj_)
            obj_.original_tagname_ = 'Enm'
        elif nodeName_ == 'Txt':
            obj_ = Txt.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Txt.append(obj_)
            obj_.original_tagname_ = 'Txt'
        elif nodeName_ == 'Rel':
            obj_ = Rel.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Rel.append(obj_)
            obj_.original_tagname_ = 'Rel'
        elif nodeName_ == 'Tim':
            obj_ = Tim.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Tim.append(obj_)
            obj_.original_tagname_ = 'Tim'
        elif nodeName_ == 'List':
            obj_ = List.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.List.append(obj_)
            obj_.original_tagname_ = 'List'
        elif nodeName_ == 'Obj':
            obj_ = Obj.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Obj.append(obj_)
            obj_.original_tagname_ = 'Obj'
# end class basicElements


class In(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Absolute=None, Activity=None, Alternative=None, Binary=None, Enumeration=None, ListEntity=None, ObjectEntity=None, Relative=None, Text=None, Time=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Absolute is None:
            self.Absolute = []
        else:
            self.Absolute = Absolute
        self.Absolute_nsprefix_ = None
        if Activity is None:
            self.Activity = []
        else:
            self.Activity = Activity
        self.Activity_nsprefix_ = None
        if Alternative is None:
            self.Alternative = []
        else:
            self.Alternative = Alternative
        self.Alternative_nsprefix_ = None
        if Binary is None:
            self.Binary = []
        else:
            self.Binary = Binary
        self.Binary_nsprefix_ = None
        if Enumeration is None:
            self.Enumeration = []
        else:
            self.Enumeration = Enumeration
        self.Enumeration_nsprefix_ = None
        if ListEntity is None:
            self.ListEntity = []
        else:
            self.ListEntity = ListEntity
        self.ListEntity_nsprefix_ = None
        if ObjectEntity is None:
            self.ObjectEntity = []
        else:
            self.ObjectEntity = ObjectEntity
        self.ObjectEntity_nsprefix_ = None
        if Relative is None:
            self.Relative = []
        else:
            self.Relative = Relative
        self.Relative_nsprefix_ = None
        if Text is None:
            self.Text = []
        else:
            self.Text = Text
        self.Text_nsprefix_ = None
        if Time is None:
            self.Time = []
        else:
            self.Time = Time
        self.Time_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, In)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if In.subclass:
            return In.subclass(*args_, **kwargs_)
        else:
            return In(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Absolute(self):
        return self.Absolute
    def set_Absolute(self, Absolute):
        self.Absolute = Absolute
    def add_Absolute(self, value):
        self.Absolute.append(value)
    def insert_Absolute_at(self, index, value):
        self.Absolute.insert(index, value)
    def replace_Absolute_at(self, index, value):
        self.Absolute[index] = value
    def get_Activity(self):
        return self.Activity
    def set_Activity(self, Activity):
        self.Activity = Activity
    def add_Activity(self, value):
        self.Activity.append(value)
    def insert_Activity_at(self, index, value):
        self.Activity.insert(index, value)
    def replace_Activity_at(self, index, value):
        self.Activity[index] = value
    def get_Alternative(self):
        return self.Alternative
    def set_Alternative(self, Alternative):
        self.Alternative = Alternative
    def add_Alternative(self, value):
        self.Alternative.append(value)
    def insert_Alternative_at(self, index, value):
        self.Alternative.insert(index, value)
    def replace_Alternative_at(self, index, value):
        self.Alternative[index] = value
    def get_Binary(self):
        return self.Binary
    def set_Binary(self, Binary):
        self.Binary = Binary
    def add_Binary(self, value):
        self.Binary.append(value)
    def insert_Binary_at(self, index, value):
        self.Binary.insert(index, value)
    def replace_Binary_at(self, index, value):
        self.Binary[index] = value
    def get_Enumeration(self):
        return self.Enumeration
    def set_Enumeration(self, Enumeration):
        self.Enumeration = Enumeration
    def add_Enumeration(self, value):
        self.Enumeration.append(value)
    def insert_Enumeration_at(self, index, value):
        self.Enumeration.insert(index, value)
    def replace_Enumeration_at(self, index, value):
        self.Enumeration[index] = value
    def get_ListEntity(self):
        return self.ListEntity
    def set_ListEntity(self, ListEntity):
        self.ListEntity = ListEntity
    def add_ListEntity(self, value):
        self.ListEntity.append(value)
    def insert_ListEntity_at(self, index, value):
        self.ListEntity.insert(index, value)
    def replace_ListEntity_at(self, index, value):
        self.ListEntity[index] = value
    def get_ObjectEntity(self):
        return self.ObjectEntity
    def set_ObjectEntity(self, ObjectEntity):
        self.ObjectEntity = ObjectEntity
    def add_ObjectEntity(self, value):
        self.ObjectEntity.append(value)
    def insert_ObjectEntity_at(self, index, value):
        self.ObjectEntity.insert(index, value)
    def replace_ObjectEntity_at(self, index, value):
        self.ObjectEntity[index] = value
    def get_Relative(self):
        return self.Relative
    def set_Relative(self, Relative):
        self.Relative = Relative
    def add_Relative(self, value):
        self.Relative.append(value)
    def insert_Relative_at(self, index, value):
        self.Relative.insert(index, value)
    def replace_Relative_at(self, index, value):
        self.Relative[index] = value
    def get_Text(self):
        return self.Text
    def set_Text(self, Text):
        self.Text = Text
    def add_Text(self, value):
        self.Text.append(value)
    def insert_Text_at(self, index, value):
        self.Text.insert(index, value)
    def replace_Text_at(self, index, value):
        self.Text[index] = value
    def get_Time(self):
        return self.Time
    def set_Time(self, Time):
        self.Time = Time
    def add_Time(self, value):
        self.Time.append(value)
    def insert_Time_at(self, index, value):
        self.Time.insert(index, value)
    def replace_Time_at(self, index, value):
        self.Time[index] = value
    def _hasContent(self):
        if (
            self.Absolute or
            self.Activity or
            self.Alternative or
            self.Binary or
            self.Enumeration or
            self.ListEntity or
            self.ObjectEntity or
            self.Relative or
            self.Text or
            self.Time
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='In', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('In')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'In':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='In')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='In', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='In'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='In', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Absolute_ in self.Absolute:
            namespaceprefix_ = self.Absolute_nsprefix_ + ':' if (UseCapturedNS_ and self.Absolute_nsprefix_) else ''
            Absolute_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Absolute', pretty_print=pretty_print)
        for Activity_ in self.Activity:
            namespaceprefix_ = self.Activity_nsprefix_ + ':' if (UseCapturedNS_ and self.Activity_nsprefix_) else ''
            Activity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Activity', pretty_print=pretty_print)
        for Alternative_ in self.Alternative:
            namespaceprefix_ = self.Alternative_nsprefix_ + ':' if (UseCapturedNS_ and self.Alternative_nsprefix_) else ''
            Alternative_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alternative', pretty_print=pretty_print)
        for Binary_ in self.Binary:
            namespaceprefix_ = self.Binary_nsprefix_ + ':' if (UseCapturedNS_ and self.Binary_nsprefix_) else ''
            Binary_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Binary', pretty_print=pretty_print)
        for Enumeration_ in self.Enumeration:
            namespaceprefix_ = self.Enumeration_nsprefix_ + ':' if (UseCapturedNS_ and self.Enumeration_nsprefix_) else ''
            Enumeration_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Enumeration', pretty_print=pretty_print)
        for ListEntity_ in self.ListEntity:
            namespaceprefix_ = self.ListEntity_nsprefix_ + ':' if (UseCapturedNS_ and self.ListEntity_nsprefix_) else ''
            ListEntity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListEntity', pretty_print=pretty_print)
        for ObjectEntity_ in self.ObjectEntity:
            namespaceprefix_ = self.ObjectEntity_nsprefix_ + ':' if (UseCapturedNS_ and self.ObjectEntity_nsprefix_) else ''
            ObjectEntity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ObjectEntity', pretty_print=pretty_print)
        for Relative_ in self.Relative:
            namespaceprefix_ = self.Relative_nsprefix_ + ':' if (UseCapturedNS_ and self.Relative_nsprefix_) else ''
            Relative_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Relative', pretty_print=pretty_print)
        for Text_ in self.Text:
            namespaceprefix_ = self.Text_nsprefix_ + ':' if (UseCapturedNS_ and self.Text_nsprefix_) else ''
            Text_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Text', pretty_print=pretty_print)
        for Time_ in self.Time:
            namespaceprefix_ = self.Time_nsprefix_ + ':' if (UseCapturedNS_ and self.Time_nsprefix_) else ''
            Time_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Time', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Absolute':
            obj_ = Absolute.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Absolute.append(obj_)
            obj_.original_tagname_ = 'Absolute'
        elif nodeName_ == 'Activity':
            obj_ = Activity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Activity.append(obj_)
            obj_.original_tagname_ = 'Activity'
        elif nodeName_ == 'Alternative':
            obj_ = Alternative.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alternative.append(obj_)
            obj_.original_tagname_ = 'Alternative'
        elif nodeName_ == 'Binary':
            obj_ = Binary.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Binary.append(obj_)
            obj_.original_tagname_ = 'Binary'
        elif nodeName_ == 'Enumeration':
            obj_ = Enumeration.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Enumeration.append(obj_)
            obj_.original_tagname_ = 'Enumeration'
        elif nodeName_ == 'ListEntity':
            obj_ = ListEntity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListEntity.append(obj_)
            obj_.original_tagname_ = 'ListEntity'
        elif nodeName_ == 'ObjectEntity':
            obj_ = ObjectEntity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ObjectEntity.append(obj_)
            obj_.original_tagname_ = 'ObjectEntity'
        elif nodeName_ == 'Relative':
            obj_ = Relative.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Relative.append(obj_)
            obj_.original_tagname_ = 'Relative'
        elif nodeName_ == 'Text':
            obj_ = Text.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Text.append(obj_)
            obj_.original_tagname_ = 'Text'
        elif nodeName_ == 'Time':
            obj_ = Time.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Time.append(obj_)
            obj_.original_tagname_ = 'Time'
# end class In


class Out(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Absolute=None, Activity=None, Alternative=None, Binary=None, Enumeration=None, ListEntity=None, ObjectEntity=None, Relative=None, Text=None, Time=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Absolute is None:
            self.Absolute = []
        else:
            self.Absolute = Absolute
        self.Absolute_nsprefix_ = None
        if Activity is None:
            self.Activity = []
        else:
            self.Activity = Activity
        self.Activity_nsprefix_ = None
        if Alternative is None:
            self.Alternative = []
        else:
            self.Alternative = Alternative
        self.Alternative_nsprefix_ = None
        if Binary is None:
            self.Binary = []
        else:
            self.Binary = Binary
        self.Binary_nsprefix_ = None
        if Enumeration is None:
            self.Enumeration = []
        else:
            self.Enumeration = Enumeration
        self.Enumeration_nsprefix_ = None
        if ListEntity is None:
            self.ListEntity = []
        else:
            self.ListEntity = ListEntity
        self.ListEntity_nsprefix_ = None
        if ObjectEntity is None:
            self.ObjectEntity = []
        else:
            self.ObjectEntity = ObjectEntity
        self.ObjectEntity_nsprefix_ = None
        if Relative is None:
            self.Relative = []
        else:
            self.Relative = Relative
        self.Relative_nsprefix_ = None
        if Text is None:
            self.Text = []
        else:
            self.Text = Text
        self.Text_nsprefix_ = None
        if Time is None:
            self.Time = []
        else:
            self.Time = Time
        self.Time_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Out)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Out.subclass:
            return Out.subclass(*args_, **kwargs_)
        else:
            return Out(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Absolute(self):
        return self.Absolute
    def set_Absolute(self, Absolute):
        self.Absolute = Absolute
    def add_Absolute(self, value):
        self.Absolute.append(value)
    def insert_Absolute_at(self, index, value):
        self.Absolute.insert(index, value)
    def replace_Absolute_at(self, index, value):
        self.Absolute[index] = value
    def get_Activity(self):
        return self.Activity
    def set_Activity(self, Activity):
        self.Activity = Activity
    def add_Activity(self, value):
        self.Activity.append(value)
    def insert_Activity_at(self, index, value):
        self.Activity.insert(index, value)
    def replace_Activity_at(self, index, value):
        self.Activity[index] = value
    def get_Alternative(self):
        return self.Alternative
    def set_Alternative(self, Alternative):
        self.Alternative = Alternative
    def add_Alternative(self, value):
        self.Alternative.append(value)
    def insert_Alternative_at(self, index, value):
        self.Alternative.insert(index, value)
    def replace_Alternative_at(self, index, value):
        self.Alternative[index] = value
    def get_Binary(self):
        return self.Binary
    def set_Binary(self, Binary):
        self.Binary = Binary
    def add_Binary(self, value):
        self.Binary.append(value)
    def insert_Binary_at(self, index, value):
        self.Binary.insert(index, value)
    def replace_Binary_at(self, index, value):
        self.Binary[index] = value
    def get_Enumeration(self):
        return self.Enumeration
    def set_Enumeration(self, Enumeration):
        self.Enumeration = Enumeration
    def add_Enumeration(self, value):
        self.Enumeration.append(value)
    def insert_Enumeration_at(self, index, value):
        self.Enumeration.insert(index, value)
    def replace_Enumeration_at(self, index, value):
        self.Enumeration[index] = value
    def get_ListEntity(self):
        return self.ListEntity
    def set_ListEntity(self, ListEntity):
        self.ListEntity = ListEntity
    def add_ListEntity(self, value):
        self.ListEntity.append(value)
    def insert_ListEntity_at(self, index, value):
        self.ListEntity.insert(index, value)
    def replace_ListEntity_at(self, index, value):
        self.ListEntity[index] = value
    def get_ObjectEntity(self):
        return self.ObjectEntity
    def set_ObjectEntity(self, ObjectEntity):
        self.ObjectEntity = ObjectEntity
    def add_ObjectEntity(self, value):
        self.ObjectEntity.append(value)
    def insert_ObjectEntity_at(self, index, value):
        self.ObjectEntity.insert(index, value)
    def replace_ObjectEntity_at(self, index, value):
        self.ObjectEntity[index] = value
    def get_Relative(self):
        return self.Relative
    def set_Relative(self, Relative):
        self.Relative = Relative
    def add_Relative(self, value):
        self.Relative.append(value)
    def insert_Relative_at(self, index, value):
        self.Relative.insert(index, value)
    def replace_Relative_at(self, index, value):
        self.Relative[index] = value
    def get_Text(self):
        return self.Text
    def set_Text(self, Text):
        self.Text = Text
    def add_Text(self, value):
        self.Text.append(value)
    def insert_Text_at(self, index, value):
        self.Text.insert(index, value)
    def replace_Text_at(self, index, value):
        self.Text[index] = value
    def get_Time(self):
        return self.Time
    def set_Time(self, Time):
        self.Time = Time
    def add_Time(self, value):
        self.Time.append(value)
    def insert_Time_at(self, index, value):
        self.Time.insert(index, value)
    def replace_Time_at(self, index, value):
        self.Time[index] = value
    def _hasContent(self):
        if (
            self.Absolute or
            self.Activity or
            self.Alternative or
            self.Binary or
            self.Enumeration or
            self.ListEntity or
            self.ObjectEntity or
            self.Relative or
            self.Text or
            self.Time
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Out', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Out')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Out':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Out')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Out', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Out'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Out', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Absolute_ in self.Absolute:
            namespaceprefix_ = self.Absolute_nsprefix_ + ':' if (UseCapturedNS_ and self.Absolute_nsprefix_) else ''
            Absolute_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Absolute', pretty_print=pretty_print)
        for Activity_ in self.Activity:
            namespaceprefix_ = self.Activity_nsprefix_ + ':' if (UseCapturedNS_ and self.Activity_nsprefix_) else ''
            Activity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Activity', pretty_print=pretty_print)
        for Alternative_ in self.Alternative:
            namespaceprefix_ = self.Alternative_nsprefix_ + ':' if (UseCapturedNS_ and self.Alternative_nsprefix_) else ''
            Alternative_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alternative', pretty_print=pretty_print)
        for Binary_ in self.Binary:
            namespaceprefix_ = self.Binary_nsprefix_ + ':' if (UseCapturedNS_ and self.Binary_nsprefix_) else ''
            Binary_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Binary', pretty_print=pretty_print)
        for Enumeration_ in self.Enumeration:
            namespaceprefix_ = self.Enumeration_nsprefix_ + ':' if (UseCapturedNS_ and self.Enumeration_nsprefix_) else ''
            Enumeration_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Enumeration', pretty_print=pretty_print)
        for ListEntity_ in self.ListEntity:
            namespaceprefix_ = self.ListEntity_nsprefix_ + ':' if (UseCapturedNS_ and self.ListEntity_nsprefix_) else ''
            ListEntity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListEntity', pretty_print=pretty_print)
        for ObjectEntity_ in self.ObjectEntity:
            namespaceprefix_ = self.ObjectEntity_nsprefix_ + ':' if (UseCapturedNS_ and self.ObjectEntity_nsprefix_) else ''
            ObjectEntity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ObjectEntity', pretty_print=pretty_print)
        for Relative_ in self.Relative:
            namespaceprefix_ = self.Relative_nsprefix_ + ':' if (UseCapturedNS_ and self.Relative_nsprefix_) else ''
            Relative_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Relative', pretty_print=pretty_print)
        for Text_ in self.Text:
            namespaceprefix_ = self.Text_nsprefix_ + ':' if (UseCapturedNS_ and self.Text_nsprefix_) else ''
            Text_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Text', pretty_print=pretty_print)
        for Time_ in self.Time:
            namespaceprefix_ = self.Time_nsprefix_ + ':' if (UseCapturedNS_ and self.Time_nsprefix_) else ''
            Time_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Time', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Absolute':
            obj_ = Absolute.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Absolute.append(obj_)
            obj_.original_tagname_ = 'Absolute'
        elif nodeName_ == 'Activity':
            obj_ = Activity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Activity.append(obj_)
            obj_.original_tagname_ = 'Activity'
        elif nodeName_ == 'Alternative':
            obj_ = Alternative.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alternative.append(obj_)
            obj_.original_tagname_ = 'Alternative'
        elif nodeName_ == 'Binary':
            obj_ = Binary.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Binary.append(obj_)
            obj_.original_tagname_ = 'Binary'
        elif nodeName_ == 'Enumeration':
            obj_ = Enumeration.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Enumeration.append(obj_)
            obj_.original_tagname_ = 'Enumeration'
        elif nodeName_ == 'ListEntity':
            obj_ = ListEntity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListEntity.append(obj_)
            obj_.original_tagname_ = 'ListEntity'
        elif nodeName_ == 'ObjectEntity':
            obj_ = ObjectEntity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ObjectEntity.append(obj_)
            obj_.original_tagname_ = 'ObjectEntity'
        elif nodeName_ == 'Relative':
            obj_ = Relative.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Relative.append(obj_)
            obj_.original_tagname_ = 'Relative'
        elif nodeName_ == 'Text':
            obj_ = Text.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Text.append(obj_)
            obj_.original_tagname_ = 'Text'
        elif nodeName_ == 'Time':
            obj_ = Time.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Time.append(obj_)
            obj_.original_tagname_ = 'Time'
# end class Out


class Choice(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, typeRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.typeRef = _cast(None, typeRef)
        self.typeRef_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Choice)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Choice.subclass:
            return Choice.subclass(*args_, **kwargs_)
        else:
            return Choice(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_typeRef(self):
        return self.typeRef
    def set_typeRef(self, typeRef):
        self.typeRef = typeRef
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Choice', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Choice')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Choice':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Choice')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Choice', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Choice'):
        if self.typeRef is not None and 'typeRef' not in already_processed:
            already_processed.add('typeRef')
            outfile.write(' typeRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.typeRef), input_name='typeRef')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Choice', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('typeRef', node)
        if value is not None and 'typeRef' not in already_processed:
            already_processed.add('typeRef')
            self.typeRef = value
            self.typeRef = ' '.join(self.typeRef.split())
            self.validate_nameType(self.typeRef)    # validate type nameType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Choice


class Member(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Member)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Member.subclass:
            return Member.subclass(*args_, **kwargs_)
        else:
            return Member(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def validate_identifierType(self, value):
        # Validate type identifierType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on identifierType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on identifierType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_identifierType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_identifierType_patterns_, ))
    validate_identifierType_patterns_ = [['^([A-Za-z0-9_]+)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Member', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Member')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Member':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Member')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Member', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Member'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Member', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
            self.id = ' '.join(self.id.split())
            self.validate_identifierType(self.id)    # validate type identifierType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Member


class basicInterfaceElementAttributes(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, basicInterfaceElementAttributes)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if basicInterfaceElementAttributes.subclass:
            return basicInterfaceElementAttributes.subclass(*args_, **kwargs_)
        else:
            return basicInterfaceElementAttributes(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='basicInterfaceElementAttributes', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('basicInterfaceElementAttributes')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'basicInterfaceElementAttributes':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='basicInterfaceElementAttributes')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='basicInterfaceElementAttributes', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='basicInterfaceElementAttributes'):
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='basicInterfaceElementAttributes', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class basicInterfaceElementAttributes


class basicMemberAttributes(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, required=True, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.required = _cast(bool, required)
        self.required_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, basicMemberAttributes)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if basicMemberAttributes.subclass:
            return basicMemberAttributes.subclass(*args_, **kwargs_)
        else:
            return basicMemberAttributes(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_required(self):
        return self.required
    def set_required(self, required):
        self.required = required
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='basicMemberAttributes', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('basicMemberAttributes')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'basicMemberAttributes':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='basicMemberAttributes')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='basicMemberAttributes', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='basicMemberAttributes'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if not self.required and 'required' not in already_processed:
            already_processed.add('required')
            outfile.write(' required="%s"' % self.gds_format_boolean(self.required, input_name='required'))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='basicMemberAttributes', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('required', node)
        if value is not None and 'required' not in already_processed:
            already_processed.add('required')
            if value in ('true', '1'):
                self.required = True
            elif value in ('false', '0'):
                self.required = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class basicMemberAttributes


class InitType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InitType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InitType.subclass:
            return InitType.subclass(*args_, **kwargs_)
        else:
            return InitType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='InitType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InitType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InitType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InitType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InitType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InitType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='InitType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class InitType


class ByeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ByeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ByeType.subclass:
            return ByeType.subclass(*args_, **kwargs_)
        else:
            return ByeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ByeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ByeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ByeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ByeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ByeType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ByeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ByeType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ByeType


class DatalossType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DatalossType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DatalossType.subclass:
            return DatalossType.subclass(*args_, **kwargs_)
        else:
            return DatalossType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DatalossType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DatalossType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DatalossType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DatalossType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DatalossType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DatalossType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DatalossType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DatalossType


class AliveType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AliveType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AliveType.subclass:
            return AliveType.subclass(*args_, **kwargs_)
        else:
            return AliveType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AliveType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AliveType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AliveType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AliveType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AliveType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AliveType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AliveType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class AliveType


class ObjectEntity(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, typeRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ObjectEntity"), self).__init__(name, required,  **kwargs_)
        self.typeRef = _cast(None, typeRef)
        self.typeRef_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectEntity)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectEntity.subclass:
            return ObjectEntity.subclass(*args_, **kwargs_)
        else:
            return ObjectEntity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_typeRef(self):
        return self.typeRef
    def set_typeRef(self, typeRef):
        self.typeRef = typeRef
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (
            super(ObjectEntity, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectEntity', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectEntity')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectEntity':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectEntity')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ObjectEntity', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ObjectEntity'):
        super(ObjectEntity, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectEntity')
        if self.typeRef is not None and 'typeRef' not in already_processed:
            already_processed.add('typeRef')
            outfile.write(' typeRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.typeRef), input_name='typeRef')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectEntity', fromsubclass_=False, pretty_print=True):
        super(ObjectEntity, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('typeRef', node)
        if value is not None and 'typeRef' not in already_processed:
            already_processed.add('typeRef')
            self.typeRef = value
            self.typeRef = ' '.join(self.typeRef.split())
            self.validate_nameType(self.typeRef)    # validate type nameType
        super(ObjectEntity, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(ObjectEntity, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class ObjectEntity


class ListEntity(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, typeRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ListEntity"), self).__init__(name, required,  **kwargs_)
        self.typeRef = _cast(None, typeRef)
        self.typeRef_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListEntity)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListEntity.subclass:
            return ListEntity.subclass(*args_, **kwargs_)
        else:
            return ListEntity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_typeRef(self):
        return self.typeRef
    def set_typeRef(self, typeRef):
        self.typeRef = typeRef
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (
            super(ListEntity, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ListEntity', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListEntity')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListEntity':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListEntity')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListEntity', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListEntity'):
        super(ListEntity, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListEntity')
        if self.typeRef is not None and 'typeRef' not in already_processed:
            already_processed.add('typeRef')
            outfile.write(' typeRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.typeRef), input_name='typeRef')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ListEntity', fromsubclass_=False, pretty_print=True):
        super(ListEntity, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('typeRef', node)
        if value is not None and 'typeRef' not in already_processed:
            already_processed.add('typeRef')
            self.typeRef = value
            self.typeRef = ' '.join(self.typeRef.split())
            self.validate_nameType(self.typeRef)    # validate type nameType
        super(ListEntity, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(ListEntity, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class ListEntity


class Time(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, isLocalTime=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Time"), self).__init__(name, required,  **kwargs_)
        self.isLocalTime = _cast(bool, isLocalTime)
        self.isLocalTime_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Time)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Time.subclass:
            return Time.subclass(*args_, **kwargs_)
        else:
            return Time(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_isLocalTime(self):
        return self.isLocalTime
    def set_isLocalTime(self, isLocalTime):
        self.isLocalTime = isLocalTime
    def _hasContent(self):
        if (
            super(Time, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Time', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Time')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Time':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Time')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Time', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Time'):
        super(Time, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Time')
        if self.isLocalTime is not None and 'isLocalTime' not in already_processed:
            already_processed.add('isLocalTime')
            outfile.write(' isLocalTime="%s"' % self.gds_format_boolean(self.isLocalTime, input_name='isLocalTime'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Time', fromsubclass_=False, pretty_print=True):
        super(Time, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('isLocalTime', node)
        if value is not None and 'isLocalTime' not in already_processed:
            already_processed.add('isLocalTime')
            if value in ('true', '1'):
                self.isLocalTime = True
            elif value in ('false', '0'):
                self.isLocalTime = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(Time, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Time, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Time


class Text(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, regExp='.*', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Text"), self).__init__(name, required,  **kwargs_)
        self.regExp = _cast(None, regExp)
        self.regExp_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Text)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Text.subclass:
            return Text.subclass(*args_, **kwargs_)
        else:
            return Text(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_regExp(self):
        return self.regExp
    def set_regExp(self, regExp):
        self.regExp = regExp
    def _hasContent(self):
        if (
            super(Text, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Text', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Text')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Text':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Text')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Text', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Text'):
        super(Text, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Text')
        if self.regExp != ".*" and 'regExp' not in already_processed:
            already_processed.add('regExp')
            outfile.write(' regExp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.regExp), input_name='regExp')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Text', fromsubclass_=False, pretty_print=True):
        super(Text, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('regExp', node)
        if value is not None and 'regExp' not in already_processed:
            already_processed.add('regExp')
            self.regExp = value
        super(Text, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Text, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Text


class Relative(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, min=None, max=None, minLabel=None, maxLabel=None, resolution=0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Relative"), self).__init__(name, required,  **kwargs_)
        self.min = _cast(float, min)
        self.min_nsprefix_ = None
        self.max = _cast(float, max)
        self.max_nsprefix_ = None
        self.minLabel = _cast(None, minLabel)
        self.minLabel_nsprefix_ = None
        self.maxLabel = _cast(None, maxLabel)
        self.maxLabel_nsprefix_ = None
        self.resolution = _cast(float, resolution)
        self.resolution_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Relative)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Relative.subclass:
            return Relative.subclass(*args_, **kwargs_)
        else:
            return Relative(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_min(self):
        return self.min
    def set_min(self, min):
        self.min = min
    def get_max(self):
        return self.max
    def set_max(self, max):
        self.max = max
    def get_minLabel(self):
        return self.minLabel
    def set_minLabel(self, minLabel):
        self.minLabel = minLabel
    def get_maxLabel(self):
        return self.maxLabel
    def set_maxLabel(self, maxLabel):
        self.maxLabel = maxLabel
    def get_resolution(self):
        return self.resolution
    def set_resolution(self, resolution):
        self.resolution = resolution
    def validate_identifierType(self, value):
        # Validate type identifierType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on identifierType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on identifierType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_identifierType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_identifierType_patterns_, ))
    validate_identifierType_patterns_ = [['^([A-Za-z0-9_]+)$']]
    def _hasContent(self):
        if (
            super(Relative, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Relative', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Relative')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Relative':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Relative')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Relative', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Relative'):
        super(Relative, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Relative')
        if self.min is not None and 'min' not in already_processed:
            already_processed.add('min')
            outfile.write(' min="%s"' % self.gds_format_double(self.min, input_name='min'))
        if self.max is not None and 'max' not in already_processed:
            already_processed.add('max')
            outfile.write(' max="%s"' % self.gds_format_double(self.max, input_name='max'))
        if self.minLabel is not None and 'minLabel' not in already_processed:
            already_processed.add('minLabel')
            outfile.write(' minLabel=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.minLabel), input_name='minLabel')), ))
        if self.maxLabel is not None and 'maxLabel' not in already_processed:
            already_processed.add('maxLabel')
            outfile.write(' maxLabel=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.maxLabel), input_name='maxLabel')), ))
        if self.resolution != 0 and 'resolution' not in already_processed:
            already_processed.add('resolution')
            outfile.write(' resolution="%s"' % self.gds_format_double(self.resolution, input_name='resolution'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Relative', fromsubclass_=False, pretty_print=True):
        super(Relative, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('min', node)
        if value is not None and 'min' not in already_processed:
            already_processed.add('min')
            value = self.gds_parse_double(value, node, 'min')
            self.min = value
        value = find_attr_value_('max', node)
        if value is not None and 'max' not in already_processed:
            already_processed.add('max')
            value = self.gds_parse_double(value, node, 'max')
            self.max = value
        value = find_attr_value_('minLabel', node)
        if value is not None and 'minLabel' not in already_processed:
            already_processed.add('minLabel')
            self.minLabel = value
            self.minLabel = ' '.join(self.minLabel.split())
            self.validate_identifierType(self.minLabel)    # validate type identifierType
        value = find_attr_value_('maxLabel', node)
        if value is not None and 'maxLabel' not in already_processed:
            already_processed.add('maxLabel')
            self.maxLabel = value
            self.maxLabel = ' '.join(self.maxLabel.split())
            self.validate_identifierType(self.maxLabel)    # validate type identifierType
        value = find_attr_value_('resolution', node)
        if value is not None and 'resolution' not in already_processed:
            already_processed.add('resolution')
            value = self.gds_parse_double(value, node, 'resolution')
            self.resolution = value
        super(Relative, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Relative, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Relative


class Enumeration(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, Member=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Enumeration"), self).__init__(name, required,  **kwargs_)
        if Member is None:
            self.Member = []
        else:
            self.Member = Member
        self.Member_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Enumeration)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Enumeration.subclass:
            return Enumeration.subclass(*args_, **kwargs_)
        else:
            return Enumeration(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Member(self):
        return self.Member
    def set_Member(self, Member):
        self.Member = Member
    def add_Member(self, value):
        self.Member.append(value)
    def insert_Member_at(self, index, value):
        self.Member.insert(index, value)
    def replace_Member_at(self, index, value):
        self.Member[index] = value
    def _hasContent(self):
        if (
            self.Member or
            super(Enumeration, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Enumeration', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Enumeration')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Enumeration':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Enumeration')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Enumeration', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Enumeration'):
        super(Enumeration, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Enumeration')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Enumeration', fromsubclass_=False, pretty_print=True):
        super(Enumeration, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Member_ in self.Member:
            namespaceprefix_ = self.Member_nsprefix_ + ':' if (UseCapturedNS_ and self.Member_nsprefix_) else ''
            Member_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Member', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(Enumeration, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Member':
            obj_ = Member.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Member.append(obj_)
            obj_.original_tagname_ = 'Member'
        super(Enumeration, self)._buildChildren(child_, node, nodeName_, True)
# end class Enumeration


class Binary(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, contentType=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Binary"), self).__init__(name, required,  **kwargs_)
        self.contentType = _cast(None, contentType)
        self.contentType_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Binary)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Binary.subclass:
            return Binary.subclass(*args_, **kwargs_)
        else:
            return Binary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_contentType(self):
        return self.contentType
    def set_contentType(self, contentType):
        self.contentType = contentType
    def _hasContent(self):
        if (
            super(Binary, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Binary', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Binary')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Binary':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Binary')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Binary', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Binary'):
        super(Binary, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Binary')
        if self.contentType is not None and 'contentType' not in already_processed:
            already_processed.add('contentType')
            outfile.write(' contentType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.contentType), input_name='contentType')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Binary', fromsubclass_=False, pretty_print=True):
        super(Binary, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('contentType', node)
        if value is not None and 'contentType' not in already_processed:
            already_processed.add('contentType')
            self.contentType = value
        super(Binary, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Binary, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Binary


class Alternative(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, Choice=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Alternative"), self).__init__(name, required,  **kwargs_)
        if Choice is None:
            self.Choice = []
        else:
            self.Choice = Choice
        self.Choice_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Alternative)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Alternative.subclass:
            return Alternative.subclass(*args_, **kwargs_)
        else:
            return Alternative(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Choice(self):
        return self.Choice
    def set_Choice(self, Choice):
        self.Choice = Choice
    def add_Choice(self, value):
        self.Choice.append(value)
    def insert_Choice_at(self, index, value):
        self.Choice.insert(index, value)
    def replace_Choice_at(self, index, value):
        self.Choice[index] = value
    def _hasContent(self):
        if (
            self.Choice or
            super(Alternative, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Alternative', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Alternative')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Alternative':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Alternative')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Alternative', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Alternative'):
        super(Alternative, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Alternative')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Alternative', fromsubclass_=False, pretty_print=True):
        super(Alternative, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Choice_ in self.Choice:
            namespaceprefix_ = self.Choice_nsprefix_ + ':' if (UseCapturedNS_ and self.Choice_nsprefix_) else ''
            Choice_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Choice', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(Alternative, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Choice':
            obj_ = Choice.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Choice.append(obj_)
            obj_.original_tagname_ = 'Choice'
        super(Alternative, self)._buildChildren(child_, node, nodeName_, True)
# end class Alternative


class Activity(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Activity"), self).__init__(name, required,  **kwargs_)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Activity)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Activity.subclass:
            return Activity.subclass(*args_, **kwargs_)
        else:
            return Activity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (
            super(Activity, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Activity', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Activity')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Activity':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Activity')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Activity', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Activity'):
        super(Activity, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Activity')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Activity', fromsubclass_=False, pretty_print=True):
        super(Activity, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(Activity, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Activity, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Activity


class Absolute(basicMemberAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicMemberAttributes
    def __init__(self, name=None, required=True, unit=None, min=-0, max=60, resolution=0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Absolute"), self).__init__(name, required,  **kwargs_)
        self.unit = _cast(None, unit)
        self.unit_nsprefix_ = None
        self.min = _cast(float, min)
        self.min_nsprefix_ = None
        self.max = _cast(float, max)
        self.max_nsprefix_ = None
        self.resolution = _cast(float, resolution)
        self.resolution_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Absolute)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Absolute.subclass:
            return Absolute.subclass(*args_, **kwargs_)
        else:
            return Absolute(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_unit(self):
        return self.unit
    def set_unit(self, unit):
        self.unit = unit
    def get_min(self):
        return self.min
    def set_min(self, min):
        self.min = min
    def get_max(self):
        return self.max
    def set_max(self, max):
        self.max = max
    def get_resolution(self):
        return self.resolution
    def set_resolution(self, resolution):
        self.resolution = resolution
    def _hasContent(self):
        if (
            super(Absolute, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Absolute', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Absolute')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Absolute':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Absolute')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Absolute', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Absolute'):
        super(Absolute, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Absolute')
        if self.unit is not None and 'unit' not in already_processed:
            already_processed.add('unit')
            outfile.write(' unit=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.unit), input_name='unit')), ))
        if self.min != -0 and 'min' not in already_processed:
            already_processed.add('min')
            outfile.write(' min="%s"' % self.gds_format_double(self.min, input_name='min'))
        if self.max != 0 and 'max' not in already_processed:
            already_processed.add('max')
            outfile.write(' max="%s"' % self.gds_format_double(self.max, input_name='max'))
        if self.resolution != 0 and 'resolution' not in already_processed:
            already_processed.add('resolution')
            outfile.write(' resolution="%s"' % self.gds_format_double(self.resolution, input_name='resolution'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Absolute', fromsubclass_=False, pretty_print=True):
        super(Absolute, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('unit', node)
        if value is not None and 'unit' not in already_processed:
            already_processed.add('unit')
            self.unit = value
        value = find_attr_value_('min', node)
        if value is not None and 'min' not in already_processed:
            already_processed.add('min')
            value = self.gds_parse_double(value, node, 'min')
            self.min = value
        value = find_attr_value_('max', node)
        if value is not None and 'max' not in already_processed:
            already_processed.add('max')
            value = self.gds_parse_double(value, node, 'max')
            self.max = value
        value = find_attr_value_('resolution', node)
        if value is not None and 'resolution' not in already_processed:
            already_processed.add('resolution')
            value = self.gds_parse_double(value, node, 'resolution')
            self.resolution = value
        super(Absolute, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Absolute, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Absolute


class Type(basicInterfaceElementAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicInterfaceElementAttributes
    def __init__(self, url=None, Absolute=None, Activity=None, Alternative=None, Binary=None, Enumeration=None, ListEntity=None, ObjectEntity=None, Relative=None, Text=None, Time=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Type"), self).__init__(url,  **kwargs_)
        if Absolute is None:
            self.Absolute = []
        else:
            self.Absolute = Absolute
        self.Absolute_nsprefix_ = None
        if Activity is None:
            self.Activity = []
        else:
            self.Activity = Activity
        self.Activity_nsprefix_ = None
        if Alternative is None:
            self.Alternative = []
        else:
            self.Alternative = Alternative
        self.Alternative_nsprefix_ = None
        if Binary is None:
            self.Binary = []
        else:
            self.Binary = Binary
        self.Binary_nsprefix_ = None
        if Enumeration is None:
            self.Enumeration = []
        else:
            self.Enumeration = Enumeration
        self.Enumeration_nsprefix_ = None
        if ListEntity is None:
            self.ListEntity = []
        else:
            self.ListEntity = ListEntity
        self.ListEntity_nsprefix_ = None
        if ObjectEntity is None:
            self.ObjectEntity = []
        else:
            self.ObjectEntity = ObjectEntity
        self.ObjectEntity_nsprefix_ = None
        if Relative is None:
            self.Relative = []
        else:
            self.Relative = Relative
        self.Relative_nsprefix_ = None
        if Text is None:
            self.Text = []
        else:
            self.Text = Text
        self.Text_nsprefix_ = None
        if Time is None:
            self.Time = []
        else:
            self.Time = Time
        self.Time_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Type)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Type.subclass:
            return Type.subclass(*args_, **kwargs_)
        else:
            return Type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Absolute(self):
        return self.Absolute
    def set_Absolute(self, Absolute):
        self.Absolute = Absolute
    def add_Absolute(self, value):
        self.Absolute.append(value)
    def insert_Absolute_at(self, index, value):
        self.Absolute.insert(index, value)
    def replace_Absolute_at(self, index, value):
        self.Absolute[index] = value
    def get_Activity(self):
        return self.Activity
    def set_Activity(self, Activity):
        self.Activity = Activity
    def add_Activity(self, value):
        self.Activity.append(value)
    def insert_Activity_at(self, index, value):
        self.Activity.insert(index, value)
    def replace_Activity_at(self, index, value):
        self.Activity[index] = value
    def get_Alternative(self):
        return self.Alternative
    def set_Alternative(self, Alternative):
        self.Alternative = Alternative
    def add_Alternative(self, value):
        self.Alternative.append(value)
    def insert_Alternative_at(self, index, value):
        self.Alternative.insert(index, value)
    def replace_Alternative_at(self, index, value):
        self.Alternative[index] = value
    def get_Binary(self):
        return self.Binary
    def set_Binary(self, Binary):
        self.Binary = Binary
    def add_Binary(self, value):
        self.Binary.append(value)
    def insert_Binary_at(self, index, value):
        self.Binary.insert(index, value)
    def replace_Binary_at(self, index, value):
        self.Binary[index] = value
    def get_Enumeration(self):
        return self.Enumeration
    def set_Enumeration(self, Enumeration):
        self.Enumeration = Enumeration
    def add_Enumeration(self, value):
        self.Enumeration.append(value)
    def insert_Enumeration_at(self, index, value):
        self.Enumeration.insert(index, value)
    def replace_Enumeration_at(self, index, value):
        self.Enumeration[index] = value
    def get_ListEntity(self):
        return self.ListEntity
    def set_ListEntity(self, ListEntity):
        self.ListEntity = ListEntity
    def add_ListEntity(self, value):
        self.ListEntity.append(value)
    def insert_ListEntity_at(self, index, value):
        self.ListEntity.insert(index, value)
    def replace_ListEntity_at(self, index, value):
        self.ListEntity[index] = value
    def get_ObjectEntity(self):
        return self.ObjectEntity
    def set_ObjectEntity(self, ObjectEntity):
        self.ObjectEntity = ObjectEntity
    def add_ObjectEntity(self, value):
        self.ObjectEntity.append(value)
    def insert_ObjectEntity_at(self, index, value):
        self.ObjectEntity.insert(index, value)
    def replace_ObjectEntity_at(self, index, value):
        self.ObjectEntity[index] = value
    def get_Relative(self):
        return self.Relative
    def set_Relative(self, Relative):
        self.Relative = Relative
    def add_Relative(self, value):
        self.Relative.append(value)
    def insert_Relative_at(self, index, value):
        self.Relative.insert(index, value)
    def replace_Relative_at(self, index, value):
        self.Relative[index] = value
    def get_Text(self):
        return self.Text
    def set_Text(self, Text):
        self.Text = Text
    def add_Text(self, value):
        self.Text.append(value)
    def insert_Text_at(self, index, value):
        self.Text.insert(index, value)
    def replace_Text_at(self, index, value):
        self.Text[index] = value
    def get_Time(self):
        return self.Time
    def set_Time(self, Time):
        self.Time = Time
    def add_Time(self, value):
        self.Time.append(value)
    def insert_Time_at(self, index, value):
        self.Time.insert(index, value)
    def replace_Time_at(self, index, value):
        self.Time[index] = value
    def _hasContent(self):
        if (
            self.Absolute or
            self.Activity or
            self.Alternative or
            self.Binary or
            self.Enumeration or
            self.ListEntity or
            self.ObjectEntity or
            self.Relative or
            self.Text or
            self.Time or
            super(Type, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Type', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Type')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Type':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Type')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Type', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Type'):
        super(Type, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Type')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Type', fromsubclass_=False, pretty_print=True):
        super(Type, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Absolute_ in self.Absolute:
            namespaceprefix_ = self.Absolute_nsprefix_ + ':' if (UseCapturedNS_ and self.Absolute_nsprefix_) else ''
            Absolute_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Absolute', pretty_print=pretty_print)
        for Activity_ in self.Activity:
            namespaceprefix_ = self.Activity_nsprefix_ + ':' if (UseCapturedNS_ and self.Activity_nsprefix_) else ''
            Activity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Activity', pretty_print=pretty_print)
        for Alternative_ in self.Alternative:
            namespaceprefix_ = self.Alternative_nsprefix_ + ':' if (UseCapturedNS_ and self.Alternative_nsprefix_) else ''
            Alternative_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alternative', pretty_print=pretty_print)
        for Binary_ in self.Binary:
            namespaceprefix_ = self.Binary_nsprefix_ + ':' if (UseCapturedNS_ and self.Binary_nsprefix_) else ''
            Binary_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Binary', pretty_print=pretty_print)
        for Enumeration_ in self.Enumeration:
            namespaceprefix_ = self.Enumeration_nsprefix_ + ':' if (UseCapturedNS_ and self.Enumeration_nsprefix_) else ''
            Enumeration_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Enumeration', pretty_print=pretty_print)
        for ListEntity_ in self.ListEntity:
            namespaceprefix_ = self.ListEntity_nsprefix_ + ':' if (UseCapturedNS_ and self.ListEntity_nsprefix_) else ''
            ListEntity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListEntity', pretty_print=pretty_print)
        for ObjectEntity_ in self.ObjectEntity:
            namespaceprefix_ = self.ObjectEntity_nsprefix_ + ':' if (UseCapturedNS_ and self.ObjectEntity_nsprefix_) else ''
            ObjectEntity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ObjectEntity', pretty_print=pretty_print)
        for Relative_ in self.Relative:
            namespaceprefix_ = self.Relative_nsprefix_ + ':' if (UseCapturedNS_ and self.Relative_nsprefix_) else ''
            Relative_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Relative', pretty_print=pretty_print)
        for Text_ in self.Text:
            namespaceprefix_ = self.Text_nsprefix_ + ':' if (UseCapturedNS_ and self.Text_nsprefix_) else ''
            Text_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Text', pretty_print=pretty_print)
        for Time_ in self.Time:
            namespaceprefix_ = self.Time_nsprefix_ + ':' if (UseCapturedNS_ and self.Time_nsprefix_) else ''
            Time_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Time', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(Type, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Absolute':
            obj_ = Absolute.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Absolute.append(obj_)
            obj_.original_tagname_ = 'Absolute'
        elif nodeName_ == 'Activity':
            obj_ = Activity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Activity.append(obj_)
            obj_.original_tagname_ = 'Activity'
        elif nodeName_ == 'Alternative':
            obj_ = Alternative.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alternative.append(obj_)
            obj_.original_tagname_ = 'Alternative'
        elif nodeName_ == 'Binary':
            obj_ = Binary.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Binary.append(obj_)
            obj_.original_tagname_ = 'Binary'
        elif nodeName_ == 'Enumeration':
            obj_ = Enumeration.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Enumeration.append(obj_)
            obj_.original_tagname_ = 'Enumeration'
        elif nodeName_ == 'ListEntity':
            obj_ = ListEntity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListEntity.append(obj_)
            obj_.original_tagname_ = 'ListEntity'
        elif nodeName_ == 'ObjectEntity':
            obj_ = ObjectEntity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ObjectEntity.append(obj_)
            obj_.original_tagname_ = 'ObjectEntity'
        elif nodeName_ == 'Relative':
            obj_ = Relative.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Relative.append(obj_)
            obj_.original_tagname_ = 'Relative'
        elif nodeName_ == 'Text':
            obj_ = Text.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Text.append(obj_)
            obj_.original_tagname_ = 'Text'
        elif nodeName_ == 'Time':
            obj_ = Time.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Time.append(obj_)
            obj_.original_tagname_ = 'Time'
        super(Type, self)._buildChildren(child_, node, nodeName_, True)
# end class Type


class Function(basicInterfaceElementAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicInterfaceElementAttributes
    def __init__(self, url=None, required='false', In=None, Out=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Function"), self).__init__(url,  **kwargs_)
        self.required = _cast(None, required)
        self.required_nsprefix_ = None
        self.In = In
        self.In_nsprefix_ = None
        self.Out = Out
        self.Out_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Function)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Function.subclass:
            return Function.subclass(*args_, **kwargs_)
        else:
            return Function(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_In(self):
        return self.In
    def set_In(self, In):
        self.In = In
    def get_Out(self):
        return self.Out
    def set_Out(self, Out):
        self.Out = Out
    def get_required(self):
        return self.required
    def set_required(self, required):
        self.required = required
    def _hasContent(self):
        if (
            self.In is not None or
            self.Out is not None or
            super(Function, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Function', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Function')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Function':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Function')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Function', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Function'):
        super(Function, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Function')
        if self.required != "false" and 'required' not in already_processed:
            already_processed.add('required')
            outfile.write(' required=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.required), input_name='required')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Function', fromsubclass_=False, pretty_print=True):
        super(Function, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.In is not None:
            namespaceprefix_ = self.In_nsprefix_ + ':' if (UseCapturedNS_ and self.In_nsprefix_) else ''
            self.In.export(outfile, level, namespaceprefix_, namespacedef_='', name_='In', pretty_print=pretty_print)
        if self.Out is not None:
            namespaceprefix_ = self.Out_nsprefix_ + ':' if (UseCapturedNS_ and self.Out_nsprefix_) else ''
            self.Out.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Out', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('required', node)
        if value is not None and 'required' not in already_processed:
            already_processed.add('required')
            self.required = value
        super(Function, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'In':
            obj_ = In.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.In = obj_
            obj_.original_tagname_ = 'In'
        elif nodeName_ == 'Out':
            obj_ = Out.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Out = obj_
            obj_.original_tagname_ = 'Out'
        super(Function, self)._buildChildren(child_, node, nodeName_, True)
# end class Function


class Object(basicInterfaceElementAttributes):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicInterfaceElementAttributes
    def __init__(self, url=None, context='global', characteristic=None, interval=0, required='false', Absolute=None, Activity=None, Alternative=None, Binary=None, Enumeration=None, ListEntity=None, ObjectEntity=None, Relative=None, Text=None, Time=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Object"), self).__init__(url,  **kwargs_)
        self.context = _cast(None, context)
        self.context_nsprefix_ = None
        self.characteristic = _cast(None, characteristic)
        self.characteristic_nsprefix_ = None
        self.interval = _cast(int, interval)
        self.interval_nsprefix_ = None
        self.required = _cast(None, required)
        self.required_nsprefix_ = None
        if Absolute is None:
            self.Absolute = []
        else:
            self.Absolute = Absolute
        self.Absolute_nsprefix_ = None
        if Activity is None:
            self.Activity = []
        else:
            self.Activity = Activity
        self.Activity_nsprefix_ = None
        if Alternative is None:
            self.Alternative = []
        else:
            self.Alternative = Alternative
        self.Alternative_nsprefix_ = None
        if Binary is None:
            self.Binary = []
        else:
            self.Binary = Binary
        self.Binary_nsprefix_ = None
        if Enumeration is None:
            self.Enumeration = []
        else:
            self.Enumeration = Enumeration
        self.Enumeration_nsprefix_ = None
        if ListEntity is None:
            self.ListEntity = []
        else:
            self.ListEntity = ListEntity
        self.ListEntity_nsprefix_ = None
        if ObjectEntity is None:
            self.ObjectEntity = []
        else:
            self.ObjectEntity = ObjectEntity
        self.ObjectEntity_nsprefix_ = None
        if Relative is None:
            self.Relative = []
        else:
            self.Relative = Relative
        self.Relative_nsprefix_ = None
        if Text is None:
            self.Text = []
        else:
            self.Text = Text
        self.Text_nsprefix_ = None
        if Time is None:
            self.Time = []
        else:
            self.Time = Time
        self.Time_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Object)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Object.subclass:
            return Object.subclass(*args_, **kwargs_)
        else:
            return Object(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Absolute(self):
        return self.Absolute
    def set_Absolute(self, Absolute):
        self.Absolute = Absolute
    def add_Absolute(self, value):
        self.Absolute.append(value)
    def insert_Absolute_at(self, index, value):
        self.Absolute.insert(index, value)
    def replace_Absolute_at(self, index, value):
        self.Absolute[index] = value
    def get_Activity(self):
        return self.Activity
    def set_Activity(self, Activity):
        self.Activity = Activity
    def add_Activity(self, value):
        self.Activity.append(value)
    def insert_Activity_at(self, index, value):
        self.Activity.insert(index, value)
    def replace_Activity_at(self, index, value):
        self.Activity[index] = value
    def get_Alternative(self):
        return self.Alternative
    def set_Alternative(self, Alternative):
        self.Alternative = Alternative
    def add_Alternative(self, value):
        self.Alternative.append(value)
    def insert_Alternative_at(self, index, value):
        self.Alternative.insert(index, value)
    def replace_Alternative_at(self, index, value):
        self.Alternative[index] = value
    def get_Binary(self):
        return self.Binary
    def set_Binary(self, Binary):
        self.Binary = Binary
    def add_Binary(self, value):
        self.Binary.append(value)
    def insert_Binary_at(self, index, value):
        self.Binary.insert(index, value)
    def replace_Binary_at(self, index, value):
        self.Binary[index] = value
    def get_Enumeration(self):
        return self.Enumeration
    def set_Enumeration(self, Enumeration):
        self.Enumeration = Enumeration
    def add_Enumeration(self, value):
        self.Enumeration.append(value)
    def insert_Enumeration_at(self, index, value):
        self.Enumeration.insert(index, value)
    def replace_Enumeration_at(self, index, value):
        self.Enumeration[index] = value
    def get_ListEntity(self):
        return self.ListEntity
    def set_ListEntity(self, ListEntity):
        self.ListEntity = ListEntity
    def add_ListEntity(self, value):
        self.ListEntity.append(value)
    def insert_ListEntity_at(self, index, value):
        self.ListEntity.insert(index, value)
    def replace_ListEntity_at(self, index, value):
        self.ListEntity[index] = value
    def get_ObjectEntity(self):
        return self.ObjectEntity
    def set_ObjectEntity(self, ObjectEntity):
        self.ObjectEntity = ObjectEntity
    def add_ObjectEntity(self, value):
        self.ObjectEntity.append(value)
    def insert_ObjectEntity_at(self, index, value):
        self.ObjectEntity.insert(index, value)
    def replace_ObjectEntity_at(self, index, value):
        self.ObjectEntity[index] = value
    def get_Relative(self):
        return self.Relative
    def set_Relative(self, Relative):
        self.Relative = Relative
    def add_Relative(self, value):
        self.Relative.append(value)
    def insert_Relative_at(self, index, value):
        self.Relative.insert(index, value)
    def replace_Relative_at(self, index, value):
        self.Relative[index] = value
    def get_Text(self):
        return self.Text
    def set_Text(self, Text):
        self.Text = Text
    def add_Text(self, value):
        self.Text.append(value)
    def insert_Text_at(self, index, value):
        self.Text.insert(index, value)
    def replace_Text_at(self, index, value):
        self.Text[index] = value
    def get_Time(self):
        return self.Time
    def set_Time(self, Time):
        self.Time = Time
    def add_Time(self, value):
        self.Time.append(value)
    def insert_Time_at(self, index, value):
        self.Time.insert(index, value)
    def replace_Time_at(self, index, value):
        self.Time[index] = value
    def get_context(self):
        return self.context
    def set_context(self, context):
        self.context = context
    def get_characteristic(self):
        return self.characteristic
    def set_characteristic(self, characteristic):
        self.characteristic = characteristic
    def get_interval(self):
        return self.interval
    def set_interval(self, interval):
        self.interval = interval
    def get_required(self):
        return self.required
    def set_required(self, required):
        self.required = required
    def validate_contextType(self, value):
        # Validate type contextType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['global', 'session']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on contextType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_characteristicType(self, value):
        # Validate type characteristicType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['static', 'dynamic', 'event']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on characteristicType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            self.Absolute or
            self.Activity or
            self.Alternative or
            self.Binary or
            self.Enumeration or
            self.ListEntity or
            self.ObjectEntity or
            self.Relative or
            self.Text or
            self.Time or
            super(Object, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Object', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Object')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Object':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Object')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Object', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Object'):
        super(Object, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Object')
        if self.context != "global" and 'context' not in already_processed:
            already_processed.add('context')
            outfile.write(' context=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.context), input_name='context')), ))
        if self.characteristic is not None and 'characteristic' not in already_processed:
            already_processed.add('characteristic')
            outfile.write(' characteristic=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.characteristic), input_name='characteristic')), ))
        if self.interval != 0 and 'interval' not in already_processed:
            already_processed.add('interval')
            outfile.write(' interval="%s"' % self.gds_format_integer(self.interval, input_name='interval'))
        if self.required != "false" and 'required' not in already_processed:
            already_processed.add('required')
            outfile.write(' required=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.required), input_name='required')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://exlap.de/v1/protocol" ', name_='Object', fromsubclass_=False, pretty_print=True):
        super(Object, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Absolute_ in self.Absolute:
            namespaceprefix_ = self.Absolute_nsprefix_ + ':' if (UseCapturedNS_ and self.Absolute_nsprefix_) else ''
            Absolute_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Absolute', pretty_print=pretty_print)
        for Activity_ in self.Activity:
            namespaceprefix_ = self.Activity_nsprefix_ + ':' if (UseCapturedNS_ and self.Activity_nsprefix_) else ''
            Activity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Activity', pretty_print=pretty_print)
        for Alternative_ in self.Alternative:
            namespaceprefix_ = self.Alternative_nsprefix_ + ':' if (UseCapturedNS_ and self.Alternative_nsprefix_) else ''
            Alternative_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alternative', pretty_print=pretty_print)
        for Binary_ in self.Binary:
            namespaceprefix_ = self.Binary_nsprefix_ + ':' if (UseCapturedNS_ and self.Binary_nsprefix_) else ''
            Binary_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Binary', pretty_print=pretty_print)
        for Enumeration_ in self.Enumeration:
            namespaceprefix_ = self.Enumeration_nsprefix_ + ':' if (UseCapturedNS_ and self.Enumeration_nsprefix_) else ''
            Enumeration_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Enumeration', pretty_print=pretty_print)
        for ListEntity_ in self.ListEntity:
            namespaceprefix_ = self.ListEntity_nsprefix_ + ':' if (UseCapturedNS_ and self.ListEntity_nsprefix_) else ''
            ListEntity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListEntity', pretty_print=pretty_print)
        for ObjectEntity_ in self.ObjectEntity:
            namespaceprefix_ = self.ObjectEntity_nsprefix_ + ':' if (UseCapturedNS_ and self.ObjectEntity_nsprefix_) else ''
            ObjectEntity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ObjectEntity', pretty_print=pretty_print)
        for Relative_ in self.Relative:
            namespaceprefix_ = self.Relative_nsprefix_ + ':' if (UseCapturedNS_ and self.Relative_nsprefix_) else ''
            Relative_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Relative', pretty_print=pretty_print)
        for Text_ in self.Text:
            namespaceprefix_ = self.Text_nsprefix_ + ':' if (UseCapturedNS_ and self.Text_nsprefix_) else ''
            Text_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Text', pretty_print=pretty_print)
        for Time_ in self.Time:
            namespaceprefix_ = self.Time_nsprefix_ + ':' if (UseCapturedNS_ and self.Time_nsprefix_) else ''
            Time_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Time', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('context', node)
        if value is not None and 'context' not in already_processed:
            already_processed.add('context')
            self.context = value
            self.validate_contextType(self.context)    # validate type contextType
        value = find_attr_value_('characteristic', node)
        if value is not None and 'characteristic' not in already_processed:
            already_processed.add('characteristic')
            self.characteristic = value
            self.validate_characteristicType(self.characteristic)    # validate type characteristicType
        value = find_attr_value_('interval', node)
        if value is not None and 'interval' not in already_processed:
            already_processed.add('interval')
            self.interval = self.gds_parse_integer(value, node, 'interval')
            if self.interval < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
        value = find_attr_value_('required', node)
        if value is not None and 'required' not in already_processed:
            already_processed.add('required')
            self.required = value
        super(Object, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Absolute':
            obj_ = Absolute.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Absolute.append(obj_)
            obj_.original_tagname_ = 'Absolute'
        elif nodeName_ == 'Activity':
            obj_ = Activity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Activity.append(obj_)
            obj_.original_tagname_ = 'Activity'
        elif nodeName_ == 'Alternative':
            obj_ = Alternative.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alternative.append(obj_)
            obj_.original_tagname_ = 'Alternative'
        elif nodeName_ == 'Binary':
            obj_ = Binary.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Binary.append(obj_)
            obj_.original_tagname_ = 'Binary'
        elif nodeName_ == 'Enumeration':
            obj_ = Enumeration.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Enumeration.append(obj_)
            obj_.original_tagname_ = 'Enumeration'
        elif nodeName_ == 'ListEntity':
            obj_ = ListEntity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListEntity.append(obj_)
            obj_.original_tagname_ = 'ListEntity'
        elif nodeName_ == 'ObjectEntity':
            obj_ = ObjectEntity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ObjectEntity.append(obj_)
            obj_.original_tagname_ = 'ObjectEntity'
        elif nodeName_ == 'Relative':
            obj_ = Relative.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Relative.append(obj_)
            obj_.original_tagname_ = 'Relative'
        elif nodeName_ == 'Text':
            obj_ = Text.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Text.append(obj_)
            obj_.original_tagname_ = 'Text'
        elif nodeName_ == 'Time':
            obj_ = Time.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Time.append(obj_)
            obj_.original_tagname_ = 'Time'
        super(Object, self)._buildChildren(child_, node, nodeName_, True)
# end class Object


class Obj(basicElements):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicElements
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Obj"), self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj,  **kwargs_)
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Obj)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Obj.subclass:
            return Obj.subclass(*args_, **kwargs_)
        else:
            return Obj(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            super(Obj, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Obj', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Obj')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Obj':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Obj')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Obj', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Obj'):
        super(Obj, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Obj')
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Obj', fromsubclass_=False, pretty_print=True):
        super(Obj, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
        super(Obj, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Obj, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Obj


class Elem(basicElements):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicElements
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Elem"), self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj,  **kwargs_)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Elem)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Elem.subclass:
            return Elem.subclass(*args_, **kwargs_)
        else:
            return Elem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (
            super(Elem, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Elem', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Elem')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Elem':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Elem')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Elem', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Elem'):
        super(Elem, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Elem')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Elem', fromsubclass_=False, pretty_print=True):
        super(Elem, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(Elem, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Elem, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Elem


class Alt(basicElements):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicElements
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, type_=None, name=None, state='ok', msg='', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Alt"), self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj,  **kwargs_)
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.msg = _cast(None, msg)
        self.msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Alt)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Alt.subclass:
            return Alt.subclass(*args_, **kwargs_)
        else:
            return Alt(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_msg(self):
        return self.msg
    def set_msg(self, msg):
        self.msg = msg
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def validate_stateType3(self, value):
        # Validate type stateType3, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ok', 'nodata', 'error']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            super(Alt, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Alt', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Alt')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Alt':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Alt')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Alt', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Alt'):
        super(Alt, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Alt')
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.state != "ok" and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.msg != "" and 'msg' not in already_processed:
            already_processed.add('msg')
            outfile.write(' msg=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.msg), input_name='msg')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Alt', fromsubclass_=False, pretty_print=True):
        super(Alt, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.type_ = ' '.join(self.type_.split())
            self.validate_nameType(self.type_)    # validate type nameType
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.name = ' '.join(self.name.split())
            self.validate_nameType(self.name)    # validate type nameType
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
            self.state = ' '.join(self.state.split())
            self.validate_stateType3(self.state)    # validate type stateType3
        value = find_attr_value_('msg', node)
        if value is not None and 'msg' not in already_processed:
            already_processed.add('msg')
            self.msg = value
        super(Alt, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Alt, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Alt


class Result(basicElements):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicElements
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, url=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Result"), self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj,  **kwargs_)
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Result)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Result.subclass:
            return Result.subclass(*args_, **kwargs_)
        else:
            return Result(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (
            super(Result, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Result', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Result')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Result':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Result')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Result', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Result'):
        super(Result, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Result')
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Result', fromsubclass_=False, pretty_print=True):
        super(Result, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
        super(Result, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Result, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Result


class ObjectData(basicElements):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicElements
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, url=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ObjectData"), self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj,  **kwargs_)
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectData.subclass:
            return ObjectData.subclass(*args_, **kwargs_)
        else:
            return ObjectData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (
            super(ObjectData, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectData', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectData')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectData':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectData')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ObjectData', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ObjectData'):
        super(ObjectData, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectData')
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectData', fromsubclass_=False, pretty_print=True):
        super(ObjectData, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
        super(ObjectData, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(ObjectData, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class ObjectData


class Call(basicElements):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicElements
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, url=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Call"), self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj,  **kwargs_)
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Call)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Call.subclass:
            return Call.subclass(*args_, **kwargs_)
        else:
            return Call(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (
            super(Call, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Call', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Call')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Call':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Call')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Call', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Call'):
        super(Call, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Call')
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Call', fromsubclass_=False, pretty_print=True):
        super(Call, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
        super(Call, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Call, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Call


class Dat(basicElements):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = basicElements
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, url=None, timeStamp='1970-01-01T00:00:00.000Z', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Dat"), self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj,  **kwargs_)
        self.url = _cast(None, url)
        self.url_nsprefix_ = None
        if isinstance(timeStamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(timeStamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = timeStamp
        self.timeStamp = initvalue_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Dat)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Dat.subclass:
            return Dat.subclass(*args_, **kwargs_)
        else:
            return Dat(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_timeStamp(self):
        return self.timeStamp
    def set_timeStamp(self, timeStamp):
        self.timeStamp = timeStamp
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nameType_patterns_, ))
    validate_nameType_patterns_ = [['^([A-Z][A-Za-z0-9_]*)$']]
    def _hasContent(self):
        if (
            super(Dat, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Dat', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Dat')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Dat':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Dat')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Dat', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Dat'):
        super(Dat, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Dat')
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.url), input_name='url')), ))
        if self.timeStamp != "1970-01-01T00:00:00.000Z" and 'timeStamp' not in already_processed:
            already_processed.add('timeStamp')
            outfile.write(' timeStamp="%s"' % self.gds_format_datetime(self.timeStamp, input_name='timeStamp'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Dat', fromsubclass_=False, pretty_print=True):
        super(Dat, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
            self.url = ' '.join(self.url.split())
            self.validate_nameType(self.url)    # validate type nameType
        value = find_attr_value_('timeStamp', node)
        if value is not None and 'timeStamp' not in already_processed:
            already_processed.add('timeStamp')
            try:
                self.timeStamp = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (timeStamp): %s' % exp)
        super(Dat, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(Dat, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class Dat


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Exlap'
        rootClass = Exlap
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Exlap'
        rootClass = Exlap
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Exlap'
        rootClass = Exlap
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Exlap'
        rootClass = Exlap
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from exlap import *\n\n')
        sys.stdout.write('import exlap as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://exlap.de/v1/protocol': [('identifierType',
                                  'schema/definitions.xsd',
                                  'ST'),
                                 ('nameType', 'schema/definitions.xsd', 'ST'),
                                 ('portableType',
                                  'schema/definitions.xsd',
                                  'ST'),
                                 ('contextType', 'schema/object.xsd', 'ST'),
                                 ('characteristicType',
                                  'schema/object.xsd',
                                  'ST'),
                                 ('basicInterfaceElementAttributes',
                                  'schema/object.xsd',
                                  'CT'),
                                 ('basicMemberAttributes',
                                  'schema/object.xsd',
                                  'CT'),
                                 ('statusType', 'schema/protocol.xsd', 'ST'),
                                 ('commandSupportedType',
                                  'schema/protocol.xsd',
                                  'ST'),
                                 ('baseValueType', 'schema/protocol.xsd', 'CT'),
                                 ('basicElements',
                                  'schema/protocol.xsd',
                                  'CT')]}

__all__ = [
    "Abs",
    "Absolute",
    "Act",
    "Activity",
    "Alive",
    "AliveType",
    "Alt",
    "Alternative",
    "Authenticate",
    "Bin",
    "Binary",
    "Bye",
    "ByeType",
    "Call",
    "Capabilities",
    "Challenge",
    "Choice",
    "Dat",
    "DatalossType",
    "Dir",
    "Elem",
    "Enm",
    "Enumeration",
    "Exlap",
    "Function",
    "Get",
    "Heartbeat",
    "In",
    "InitType",
    "Interface",
    "List",
    "ListEntity",
    "Match",
    "Member",
    "Obj",
    "Object",
    "ObjectData",
    "ObjectEntity",
    "Out",
    "Protocol",
    "Rel",
    "Relative",
    "Req",
    "Result",
    "Rsp",
    "Status",
    "Subscribe",
    "Supports",
    "Text",
    "Tim",
    "Time",
    "Txt",
    "Type",
    "Unsubscribe",
    "UrlList",
    "baseValueType",
    "basicElements",
    "basicInterfaceElementAttributes",
    "basicMemberAttributes"
]
