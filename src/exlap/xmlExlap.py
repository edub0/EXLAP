#!/usr/bin/env python

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

import os
import sys
from lxml import etree as etree_

import src.exlap.exlap as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
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
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class ExlapSub(supermod.Exlap):
    def __init__(self, Req=None, Status=None, Rsp=None, Dat=None, **kwargs_):
        super(ExlapSub, self).__init__(Req, Status, Rsp, Dat,  **kwargs_)
supermod.Exlap.subclass = ExlapSub
# end class ExlapSub


class StatusSub(supermod.Status):
    def __init__(self, msg='', Init=None, Bye=None, Dataloss=None, Alive=None, **kwargs_):
        super(StatusSub, self).__init__(msg, Init, Bye, Dataloss, Alive,  **kwargs_)
supermod.Status.subclass = StatusSub
# end class StatusSub


class ReqSub(supermod.Req):
    def __init__(self, id='0', Protocol=None, Dir=None, Subscribe=None, Unsubscribe=None, Call=None, Get=None, Bye=None, Alive=None, Heartbeat=None, Interface=None, Authenticate=None, **kwargs_):
        super(ReqSub, self).__init__(id, Protocol, Dir, Subscribe, Unsubscribe, Call, Get, Bye, Alive, Heartbeat, Interface, Authenticate,  **kwargs_)
supermod.Req.subclass = ReqSub
# end class ReqSub


class InterfaceSub(supermod.Interface):
    def __init__(self, url=None, **kwargs_):
        super(InterfaceSub, self).__init__(url,  **kwargs_)
supermod.Interface.subclass = InterfaceSub
# end class InterfaceSub


class ProtocolSub(supermod.Protocol):
    def __init__(self, version=None, returnCapabilities=False, **kwargs_):
        super(ProtocolSub, self).__init__(version, returnCapabilities,  **kwargs_)
supermod.Protocol.subclass = ProtocolSub
# end class ProtocolSub


class GetSub(supermod.Get):
    def __init__(self, url=None, **kwargs_):
        super(GetSub, self).__init__(url,  **kwargs_)
supermod.Get.subclass = GetSub
# end class GetSub


class AliveSub(supermod.Alive):
    def __init__(self, **kwargs_):
        super(AliveSub, self).__init__( **kwargs_)
supermod.Alive.subclass = AliveSub
# end class AliveSub


class HeartbeatSub(supermod.Heartbeat):
    def __init__(self, ival=None, **kwargs_):
        super(HeartbeatSub, self).__init__(ival,  **kwargs_)
supermod.Heartbeat.subclass = HeartbeatSub
# end class HeartbeatSub


class ByeSub(supermod.Bye):
    def __init__(self, **kwargs_):
        super(ByeSub, self).__init__( **kwargs_)
supermod.Bye.subclass = ByeSub
# end class ByeSub


class SubscribeSub(supermod.Subscribe):
    def __init__(self, url=None, ival='0', content=True, timeStamp='false', **kwargs_):
        super(SubscribeSub, self).__init__(url, ival, content, timeStamp,  **kwargs_)
supermod.Subscribe.subclass = SubscribeSub
# end class SubscribeSub


class AuthenticateSub(supermod.Authenticate):
    def __init__(self, phase=None, user='', cnonce='', digest='', **kwargs_):
        super(AuthenticateSub, self).__init__(phase, user, cnonce, digest,  **kwargs_)
supermod.Authenticate.subclass = AuthenticateSub
# end class AuthenticateSub


class UnsubscribeSub(supermod.Unsubscribe):
    def __init__(self, url=None, **kwargs_):
        super(UnsubscribeSub, self).__init__(url,  **kwargs_)
supermod.Unsubscribe.subclass = UnsubscribeSub
# end class UnsubscribeSub


class DirSub(supermod.Dir):
    def __init__(self, urlPattern='*', fromEntry=1, numOfEntries=999999999, **kwargs_):
        super(DirSub, self).__init__(urlPattern, fromEntry, numOfEntries,  **kwargs_)
supermod.Dir.subclass = DirSub
# end class DirSub


class RspSub(supermod.Rsp):
    def __init__(self, id='0', status='ok', msg='', Type=None, Function=None, Object=None, ObjectData=None, UrlList=None, Result=None, Challenge=None, Capabilities=None, **kwargs_):
        super(RspSub, self).__init__(id, status, msg, Type, Function, Object, ObjectData, UrlList, Result, Challenge, Capabilities,  **kwargs_)
supermod.Rsp.subclass = RspSub
# end class RspSub


class CapabilitiesSub(supermod.Capabilities):
    def __init__(self, service=None, description='', version='1.0', Supports=None, **kwargs_):
        super(CapabilitiesSub, self).__init__(service, description, version, Supports,  **kwargs_)
supermod.Capabilities.subclass = CapabilitiesSub
# end class CapabilitiesSub


class SupportsSub(supermod.Supports):
    def __init__(self, protocol=None, interface=False, authenticate=False, heartbeat=False, datTimeStamp=False, **kwargs_):
        super(SupportsSub, self).__init__(protocol, interface, authenticate, heartbeat, datTimeStamp,  **kwargs_)
supermod.Supports.subclass = SupportsSub
# end class SupportsSub


class ChallengeSub(supermod.Challenge):
    def __init__(self, nonce='', **kwargs_):
        super(ChallengeSub, self).__init__(nonce,  **kwargs_)
supermod.Challenge.subclass = ChallengeSub
# end class ChallengeSub


class UrlListSub(supermod.UrlList):
    def __init__(self, Match=None, **kwargs_):
        super(UrlListSub, self).__init__(Match,  **kwargs_)
supermod.UrlList.subclass = UrlListSub
# end class UrlListSub


class MatchSub(supermod.Match):
    def __init__(self, url=None, type_='object', isSubscribed=False, **kwargs_):
        super(MatchSub, self).__init__(url, type_, isSubscribed,  **kwargs_)
supermod.Match.subclass = MatchSub
# end class MatchSub


class baseValueTypeSub(supermod.baseValueType):
    def __init__(self, name=None, state='ok', msg='', **kwargs_):
        super(baseValueTypeSub, self).__init__(name, state, msg,  **kwargs_)
supermod.baseValueType.subclass = baseValueTypeSub
# end class baseValueTypeSub


class AbsSub(supermod.Abs):
    def __init__(self, val=0, name=None, state='ok', msg='', **kwargs_):
        super(AbsSub, self).__init__(val, name, state, msg,  **kwargs_)
supermod.Abs.subclass = AbsSub
# end class AbsSub


class ActSub(supermod.Act):
    def __init__(self, val=False, name=None, state='ok', msg='', **kwargs_):
        super(ActSub, self).__init__(val, name, state, msg,  **kwargs_)
supermod.Act.subclass = ActSub
# end class ActSub


class BinSub(supermod.Bin):
    def __init__(self, val='', name=None, state='ok', msg='', **kwargs_):
        super(BinSub, self).__init__(val, name, state, msg,  **kwargs_)
supermod.Bin.subclass = BinSub
# end class BinSub


class EnmSub(supermod.Enm):
    def __init__(self, val='default', name=None, state='ok', msg='', **kwargs_):
        super(EnmSub, self).__init__(val, name, state, msg,  **kwargs_)
supermod.Enm.subclass = EnmSub
# end class EnmSub


class TxtSub(supermod.Txt):
    def __init__(self, val='', name=None, state='ok', msg='', **kwargs_):
        super(TxtSub, self).__init__(val, name, state, msg,  **kwargs_)
supermod.Txt.subclass = TxtSub
# end class TxtSub


class RelSub(supermod.Rel):
    def __init__(self, val=0, name=None, state='ok', msg='', **kwargs_):
        super(RelSub, self).__init__(val, name, state, msg,  **kwargs_)
supermod.Rel.subclass = RelSub
# end class RelSub


class TimSub(supermod.Tim):
    def __init__(self, val='1970-01-01T00:00:00.000Z', name=None, state='ok', msg='', **kwargs_):
        super(TimSub, self).__init__(val, name, state, msg,  **kwargs_)
supermod.Tim.subclass = TimSub
# end class TimSub


class ListSub(supermod.List):
    def __init__(self, name=None, state='ok', msg='', Elem=None, **kwargs_):
        super(ListSub, self).__init__(name, state, msg, Elem,  **kwargs_)
supermod.List.subclass = ListSub
# end class ListSub


class basicElementsSub(supermod.basicElements):
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, extensiontype_=None, **kwargs_):
        super(basicElementsSub, self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj, extensiontype_,  **kwargs_)
supermod.basicElements.subclass = basicElementsSub
# end class basicElementsSub


class InSub(supermod.In):
    def __init__(self, Absolute=None, Activity=None, Alternative=None, Binary=None, Enumeration=None, ListEntity=None, ObjectEntity=None, Relative=None, Text=None, Time=None, **kwargs_):
        super(InSub, self).__init__(Absolute, Activity, Alternative, Binary, Enumeration, ListEntity, ObjectEntity, Relative, Text, Time,  **kwargs_)
supermod.In.subclass = InSub
# end class InSub


class OutSub(supermod.Out):
    def __init__(self, Absolute=None, Activity=None, Alternative=None, Binary=None, Enumeration=None, ListEntity=None, ObjectEntity=None, Relative=None, Text=None, Time=None, **kwargs_):
        super(OutSub, self).__init__(Absolute, Activity, Alternative, Binary, Enumeration, ListEntity, ObjectEntity, Relative, Text, Time,  **kwargs_)
supermod.Out.subclass = OutSub
# end class OutSub


class ChoiceSub(supermod.Choice):
    def __init__(self, typeRef=None, **kwargs_):
        super(ChoiceSub, self).__init__(typeRef,  **kwargs_)
supermod.Choice.subclass = ChoiceSub
# end class ChoiceSub


class MemberSub(supermod.Member):
    def __init__(self, id=None, **kwargs_):
        super(MemberSub, self).__init__(id,  **kwargs_)
supermod.Member.subclass = MemberSub
# end class MemberSub


class basicInterfaceElementAttributesSub(supermod.basicInterfaceElementAttributes):
    def __init__(self, url=None, extensiontype_=None, **kwargs_):
        super(basicInterfaceElementAttributesSub, self).__init__(url, extensiontype_,  **kwargs_)
supermod.basicInterfaceElementAttributes.subclass = basicInterfaceElementAttributesSub
# end class basicInterfaceElementAttributesSub


class basicMemberAttributesSub(supermod.basicMemberAttributes):
    def __init__(self, name=None, required=True, extensiontype_=None, **kwargs_):
        super(basicMemberAttributesSub, self).__init__(name, required, extensiontype_,  **kwargs_)
supermod.basicMemberAttributes.subclass = basicMemberAttributesSub
# end class basicMemberAttributesSub


class InitTypeSub(supermod.InitType):
    def __init__(self, **kwargs_):
        super(InitTypeSub, self).__init__( **kwargs_)
supermod.InitType.subclass = InitTypeSub
# end class InitTypeSub


class ByeTypeSub(supermod.ByeType):
    def __init__(self, **kwargs_):
        super(ByeTypeSub, self).__init__( **kwargs_)
supermod.ByeType.subclass = ByeTypeSub
# end class ByeTypeSub


class DatalossTypeSub(supermod.DatalossType):
    def __init__(self, **kwargs_):
        super(DatalossTypeSub, self).__init__( **kwargs_)
supermod.DatalossType.subclass = DatalossTypeSub
# end class DatalossTypeSub


class AliveTypeSub(supermod.AliveType):
    def __init__(self, **kwargs_):
        super(AliveTypeSub, self).__init__( **kwargs_)
supermod.AliveType.subclass = AliveTypeSub
# end class AliveTypeSub


class ObjectEntitySub(supermod.ObjectEntity):
    def __init__(self, name=None, required=True, typeRef=None, **kwargs_):
        super(ObjectEntitySub, self).__init__(name, required, typeRef,  **kwargs_)
supermod.ObjectEntity.subclass = ObjectEntitySub
# end class ObjectEntitySub


class ListEntitySub(supermod.ListEntity):
    def __init__(self, name=None, required=True, typeRef=None, **kwargs_):
        super(ListEntitySub, self).__init__(name, required, typeRef,  **kwargs_)
supermod.ListEntity.subclass = ListEntitySub
# end class ListEntitySub


class TimeSub(supermod.Time):
    def __init__(self, name=None, required=True, isLocalTime=None, **kwargs_):
        super(TimeSub, self).__init__(name, required, isLocalTime,  **kwargs_)
supermod.Time.subclass = TimeSub
# end class TimeSub


class TextSub(supermod.Text):
    def __init__(self, name=None, required=True, regExp='.*', **kwargs_):
        super(TextSub, self).__init__(name, required, regExp,  **kwargs_)
supermod.Text.subclass = TextSub
# end class TextSub


class RelativeSub(supermod.Relative):
    def __init__(self, name=None, required=True, min=None, max=None, minLabel=None, maxLabel=None, resolution=0, **kwargs_):
        super(RelativeSub, self).__init__(name, required, min, max, minLabel, maxLabel, resolution,  **kwargs_)
supermod.Relative.subclass = RelativeSub
# end class RelativeSub


class EnumerationSub(supermod.Enumeration):
    def __init__(self, name=None, required=True, Member=None, **kwargs_):
        super(EnumerationSub, self).__init__(name, required, Member,  **kwargs_)
supermod.Enumeration.subclass = EnumerationSub
# end class EnumerationSub


class BinarySub(supermod.Binary):
    def __init__(self, name=None, required=True, contentType=None, **kwargs_):
        super(BinarySub, self).__init__(name, required, contentType,  **kwargs_)
supermod.Binary.subclass = BinarySub
# end class BinarySub


class AlternativeSub(supermod.Alternative):
    def __init__(self, name=None, required=True, Choice=None, **kwargs_):
        super(AlternativeSub, self).__init__(name, required, Choice,  **kwargs_)
supermod.Alternative.subclass = AlternativeSub
# end class AlternativeSub


class ActivitySub(supermod.Activity):
    def __init__(self, name=None, required=True, **kwargs_):
        super(ActivitySub, self).__init__(name, required,  **kwargs_)
supermod.Activity.subclass = ActivitySub
# end class ActivitySub


class AbsoluteSub(supermod.Absolute):
    def __init__(self, name=None, required=True, unit=None, min=0, max=0, resolution=0, **kwargs_):
        super(AbsoluteSub, self).__init__(name, required, unit, min, max, resolution,  **kwargs_)
supermod.Absolute.subclass = AbsoluteSub
# end class AbsoluteSub


class TypeSub(supermod.Type):
    def __init__(self, url=None, Absolute=None, Activity=None, Alternative=None, Binary=None, Enumeration=None, ListEntity=None, ObjectEntity=None, Relative=None, Text=None, Time=None, **kwargs_):
        super(TypeSub, self).__init__(url, Absolute, Activity, Alternative, Binary, Enumeration, ListEntity, ObjectEntity, Relative, Text, Time,  **kwargs_)
supermod.Type.subclass = TypeSub
# end class TypeSub


class FunctionSub(supermod.Function):
    def __init__(self, url=None, required='false', In=None, Out=None, **kwargs_):
        super(FunctionSub, self).__init__(url, required, In, Out,  **kwargs_)
supermod.Function.subclass = FunctionSub
# end class FunctionSub


class ObjectSub(supermod.Object):
    def __init__(self, url=None, context='global', characteristic=None, interval=0, required='false', Absolute=None, Activity=None, Alternative=None, Binary=None, Enumeration=None, ListEntity=None, ObjectEntity=None, Relative=None, Text=None, Time=None, **kwargs_):
        super(ObjectSub, self).__init__(url, context, characteristic, interval, required, Absolute, Activity, Alternative, Binary, Enumeration, ListEntity, ObjectEntity, Relative, Text, Time,  **kwargs_)
supermod.Object.subclass = ObjectSub
# end class ObjectSub


class ObjSub(supermod.Obj):
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, name=None, state='ok', msg='', **kwargs_):
        super(ObjSub, self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj, name, state, msg,  **kwargs_)
supermod.Obj.subclass = ObjSub
# end class ObjSub


class ElemSub(supermod.Elem):
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, **kwargs_):
        super(ElemSub, self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj,  **kwargs_)
supermod.Elem.subclass = ElemSub
# end class ElemSub


class AltSub(supermod.Alt):
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, type_=None, name=None, state='ok', msg='', **kwargs_):
        super(AltSub, self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj, type_, name, state, msg,  **kwargs_)
supermod.Alt.subclass = AltSub
# end class AltSub


class ResultSub(supermod.Result):
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, url=None, **kwargs_):
        super(ResultSub, self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj, url,  **kwargs_)
supermod.Result.subclass = ResultSub
# end class ResultSub


class ObjectDataSub(supermod.ObjectData):
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, url=None, **kwargs_):
        super(ObjectDataSub, self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj, url,  **kwargs_)
supermod.ObjectData.subclass = ObjectDataSub
# end class ObjectDataSub


class CallSub(supermod.Call):
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, url=None, **kwargs_):
        super(CallSub, self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj, url,  **kwargs_)
supermod.Call.subclass = CallSub
# end class CallSub


class DatSub(supermod.Dat):
    def __init__(self, Abs=None, Act=None, Alt=None, Bin=None, Enm=None, Txt=None, Rel=None, Tim=None, List=None, Obj=None, url=None, timeStamp='1970-01-01T00:00:00.000Z', **kwargs_):
        super(DatSub, self).__init__(Abs, Act, Alt, Bin, Enm, Txt, Rel, Tim, List, Obj, url, timeStamp,  **kwargs_)
supermod.Dat.subclass = DatSub
# end class DatSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Exlap'
        rootClass = supermod.Exlap
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Exlap'
        rootClass = supermod.Exlap
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Exlap'
        rootClass = supermod.Exlap
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Exlap'
        rootClass = supermod.Exlap
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
