from itertools import groupby


def merge_the_tools(string, k):
    i = int(len(string)/k)
    total = len(string)
    print(total)
    print(i)
    res = []
    for x in range(0, total, i):
        y = ''
        for c in string[x:x+i]:
            if c not in y:
                y += c
        else:
            res.append(y)
    # print('\n'.join(res))
merge_the_tools('KYQYTWXTDQXWDLKIXNWIITFBLIHRNGDZGVYCRXVWNUVSFFACUXMCSTFFBNWQVBQCWOEPNBOAVJUCOUGITSMNLSUOFRFAUXETNIKAJYCEJWIXSOHMGUBTOWKVPPXJOCEBKPDWNFCXDLWVZEJIALBOJLLYCIJQKOTXDWTSDVRIGOEIUPQUCRKLFVLHFXASNVPSUKKXHCGOSMYMDOIGHUTMPHWWEYORTFJNPVNXZVNTJNFMBPSIJOXAVTXZRNSKTDAKANJAKYTTLBFMSAXCOUCJNBKGPESKHSWJHGJREFKSISGASDCIZHTOKFUBJNLSFIBPQNGWSROCLVCDAHNAQGOALJCUYPOFZPUPEDMYWAAHXDKAMXACFQCQBGMZWAHVRBNYEZWABXJBCVBOSDQZTSPVZDWXFDSZHFXNGTQISZLUVMKPPAPIVGFWKCTRHNQQVPEBJULDVYAQKKGBLXMIDREPVZHFMZVJPZNAVADRZDHJOPNBMZLSQRHOQQTEQQOFSDFNDKGCOQOEFBHUASMSJTIBMDFCUVHOYOBCYKGOAWSHXBDZTPUELEFXINZEIISJYVNWFTNHQHPPJSREKNJXRQUZDVDOFVZDRMBYHOGZYXRHRILBVWYMPUOURRIWPJBIVFGFVOGTLXADHOGCMHRBDFWVYGTPQVXNCGUXUBRGYTLGJRKWADZEIVZJEUAURAJTGERCFIKFDVLNPWJPZITKGUVKPVGGXPADVTGCBQIGOTTDREUTPQFVKCFBZNKXEMAAFICIBMOPGKUZOQUDGZYTDFUDUGAZUCBZNFJQSAFAKBBYRWEYXETBMPEGWGHQKISZOBPIDWINXJORHSRFWKGIZMRXSYOEHIEXLTHPQPCPASGIMXPJJVTJHMGBLWHUELTQHAHZRJOTEXDQWSBGNXPWJXXWUHQASJSBLZCCJRWPQZFMUHSHEJEPHDMDKCDFOWIZVLEGECVUDDIXKDFQMLFVQRYDWEKMCSNZFRGJTDFZGOWSTBIFOOBHHBKDHUPJMDJSWRDSUJRDZNVSRGZHUCODGYHNUYXJDIDCZGUVRNYSAWMTCMDYORBWSKKMJJVORYQSHMNAZOTCKFVORAMISNEKAQYLZUZSUSKDEYEEMXGYEDMYEYGYNMKNDIYEEAXBSHEYHICVHKTMQHKUFSUVGEKJMLQTNNUFWYDEJIBQSVCIEOEMGAHNETYTEOMRDGYAEEGNMJGGEIRLZVXFYEUCXTVEJJXNPWPWAXLMGRUNCLYBHVIFBDJAYHGHQEWGANECMPQTJKILWIOFFWMIBVIZCPJVVHDVVHXJYPEHZMUVUKABJMJKISMMJVHGCKBZTAJSPPBOCYMYIMARZLEJFQXQNHWPRZRNBCFQRIHVGVURHWKIJOTPGRFTYCLRBEGDGLVZWEVEZRVJPIRYWLNFETAEVLXYPEBXRZXNDSSDLPMAXFYWSMBYHBCCPACGGEEXDDLIXFNIUBISHGOBURABSCFJEIQKOWITZVBWCPEWQOQZUEBRXBSQFYBKGRWUNENMBQKDFQCYESXZZYQWBKOHIQRQHNMXUBLXSWDZMFXRXVSYVKVZULGFBZXLOKKKNVIFTLFISEBPBTQZFNYBYEIADGNTSXEFSMLOZSWRYXIASYZXLXAMDJMIRBBJYHQSTDGUXENWBWYTWXSKWVWBGKJXLMILUADPEMKBQZZSVXNUWIESDCVJMEIZTSKNSPEYBOAUQBOLZBFVLLQONLZBQJALDMYWCCWFTYZJAPWZTEUERKVFWWIOGJZJVZHZDEHWCGHCYGDRKYVBKSIIPRYVCZGZYOZCUGAYOKDMQGFCGDFTVQBKHAHLBOKAELEARGYISDWIKCMSFULCKPNRRUCSKOUOAYQTHRBZUAKGCWZJQMLCBATSVXNHOHYOGOHPFLOALYGPXHAPUNSVONQLNDSBKQPSHYHMLYOYWXNTEPLYDDWRQMCDRWGDNXWWWFIJDXICWXXANIZQNXJEJNJCJQFYNDULLFXOEFSACQAPYBHMYQSJDDLPVTNLWKWHPTYTAQVDGVUHZCVZUNJYQWPOPEZMOXVFTTATKVWSTTBUVWTPJCPCZGQQLPEZOAHHVJBHFZAASBUPYNHJSWNTFFJQWORLQYSLITTPVTRNWLFWAMISKVLPBXFXNXKDXDOHYHYTCPJBAOXBAFVKDJCEIHDVGOYGTONRYMLCDUDEKDHKICWLNYRVIXQONQWGHMZFAMHDGNHSQQCYVBMIZFGJEYARPWZYIZDILMMUZVMPORQJSCTTJZDOYDHPZHPKGSURGINGGAXURNFLRYEDAJRAMYROFGYNAUHGDUOJUMFNBKYTIFWIOPKDPBRVHRIJLPQQMGBISGWWQWPZDNJSEWXTXOQHHZQUQILEPONJVJFLHWMLLYFPUEJTSZCBATXTDIXSZMEUVJFFGUSTSZJODUHXVKYYFVRIGQDFDHBASIHACZUWYDMDZUAUGYUNWLXEEALJJMLEUVEZUYVVDIYEEBZMBTZXHWDNZOYKALOXGTWDTTYZDYDHZETBAUAHTEWUSWEVHVSOQQRLJRKNPOWRSSSSMSBHYZBRVIODDGTVYMGHDRWUHTLZLFUZYXHYXKPUSFXXNSSLEZVJSREZMRAZXWZXUIVTSNNLSNIGFDRMEOVWGZXUTZUQYVNUDINXVCIOPTWXYNJCCGAKIZGBAARYVGUAOJYMMICDDYCBNNFRUFDCGKFHKYHIECKSNIGBTIFYIJAWXHPTPTXVFCERAMBEQMYDWFFPPMQYXQWUZLNOGMKLOOFQCGUSSVYPAFGPTWPQOLNOZACFPOTDDYWFEQAZNYQPFWFYVWOLIDBHGGOVUHYZHUHONHNCHDSOBZMYVCKFGNMMTBHOKHPSEWITFVXMAPABOOCMTORBBGNVHWLTFANLXVGCQERSTTWKIYWDMPENVTKCRVYWWLKVHQXZUQSQKQAUOYXCNDRJWCNNZNLXZVSIOSJIIDASTCOJANLQQFBMJQBIENGDIANWSWHBAJVVMMFOZSEQXHEIYGRCTZHDZUCSSLVUUSQGEVXEPBWNJAVJGOLZPSFPOJJIUGDOYTXFQUJFXFUIFSROIENYYUPMDYXXEAOEVNJLJUSGZPRHHIVPPKPNFECKCZKIZYPWNYJWTBEUQXDZIYRXLGKSLMCPLMAMMPIBPRXKVEFNDINLJGIUMTMZHQRVDTHRISTZJSKEWRUABHNKNWEBRSDAJWVOPDFZVYYGTKNRBHRDOHPDDUGWOJWZHSNWXTVSTWAMGNGKUXNKECPJYWHPHEOPYCLVXJPSFRHNFNZBMOMTTBERZMIJSXYQBLNYWESDVZRAOSCBHQUATYTTMCCEZCWCPJAMPUPLUINIBRLKJHKDIDYUFCZGEXIVJKHYFZLBJZJMSXWCEGFMMDHRHIALFIIOVSPARABCBMRULPWQYDCKILDPVDCDOKTLCILVJOAMCRGOGEGEHKQRYUGTZIWNVSYZALVLBXYGOGWWLCDUOTMMPUGPFEEAWFZZSWKUTKCJRYGECLYQGMFWHLNORRQQWRPROBLJMPTFPBJROHJUWOSFBFTTXJLVAAMQDZCPOVWFYFWOPIILWBQAILVFWGDWIPPLRRDFOZLOHJCWTMJSPBSYMNDIVGGDYXQPOTWEVJSCVWYOJHGYKYWWNCGIKONIMEXCZWJUFBWAAWPJFXJPWGLLKTUUIJFWPCAPAJJGNIINEXWMVFBTNPEXIAUSMZQBDRQEACMNKUAQSYCPGGKTVOTFRPYDOQERHXXKZJXLEABYAGNGMXCJNVOEKOJAFQTMNRWMCWXGYAEYITFWSHFIEWOQKYQPOJEBCAPFYOLYOSXZNEVINDQTZGJJGZBUKFXNHOSGCFGTZDSPJPZYURRTXAFEBGAOLABSOVATCHMEMGTYVSWSJOLIQQMSWPGJPJCDGEWILKMAQHYOBUGMITVBMJTIYBUNKYTQCRAQCPQUWOKYIQKTMHUYRPIPSCFEAYUDRWTTLJQIZAIJTUEFEAFVPNMHQTNSRJVLGQERBWBAXLKQIQXMRCJGPVQHPDAINXTVOAMPWQSVDENLUKXLOGUGEMNVRPFENBBDBQUZGMVJQIXNVUYJDURHGHEYWJELKGOLWJNEXIPQSMDPJDBMYSVGZZGYILJVTYGRJVXGFOWYBBNMFOAFHVLIWSGGFSBASKRBFOJLCGLFJYTOPTTYQHGMBPTGHWIZGZCMPLZTTKBDKUTZQPXGWGVZXQHEMPFTOHHFUGYOSBTCYMCOBBUZHRYEHFKUURPKYWRVESJWTEYRQCFSECTNVSUDXEZUWQGWOYRSQCQLGQFZTKTZOMMKEIPEPQANGGLUGDOYHEMQURPPDIOSUDEBNVFCLFPTNBNWGBUPHGFBXWTDGHVBMBEAYJEJQUCFXRBFSYUZGCCGYVJFFGIRJMTHXYSPUUWTNAYFAUGGWKOVGZCNFMGOAAXXAPOULKPYKNDKHLTGWJDEJFRQTXFTZESZUGVFSKEFZJRJXMPTWSZFZSVSPCNRHFQDNOIFAOMCYELVQCQOWRTVJRPAVCRCJKHWAQDAEQEEWPBMRTDNKYKVPBYLDPPMBXKDPOGVEKAAADOTXRJJQTHHXFSAWIPYHZBWNJRTUTTUZKPWDYHTUODRVVTSFKSOKVKZFEVZXQVWAKUELEZHUCYQATKHECWQXGRCMMDMDYKDJFJWLLDHNDXPWJXCLTSLBKNOYRABRKHARSWCDBMRELIBVFDGYYRAKHOIAQMRATUSNSWRUIKYUSBPYFXWFRYPYOXAEJTFENZSGVJCGVCCNETLLSKQJKFJZEJDQDKUSJOAHXCPUHRILMVWEHOOSVZRZLWRQHMIQALZAPOWWHEHTAFYJVOBQNUSARJQYXBQAMQCBGYYODHHFPHQKXSBLMVNFGEFEFYETQIUWGUMLEUSTDJFBDIORDBXKHEQMCWHSEEPKYBYEXSZDBFEENUWTVVDFZTTEPBWVFNHFRFKQYJTBQZIETGXRBCWCXPGOSFJXUQDLWPEWAXXRZFVUNUNOWLTTBBHTIQTDIYOGNUCNUCETJBNXVDNTOIORKXLSPGVYEMETGJGANNVYQLXOOLJCTYUFVHALPVJTJPMSYUULJQMCDJQRUZVQZRXVAXIPVRIEGWYHTTUELGGQQYJMAEEZWCUWZCOUVWBEVZNQUHUHOBXGBGSBNZBLBXJACXXZUYDRZQHUABDQEBWGHQHUPKFSIPVMOSLKSRBRJINJMRZSSXYBQIYHUFACWVQLPCVHVZYEHMOVDPOXPOAFYYOTGOXCLOPASLHNKIRTUHRZZHYQXYVWZLPFAMHNCZOUKXJWFDRZKKALRYBPXYLYKCDMQMZTLPPXNZVUENWQXWCRXFGWETUQVXCLLDGXVYWKZSEDHATGZXXWDFSHYOXVNBJYGPXBPULOOQTVSNDRKBNPIHWHXVCKYLJFDIGUCULQKENCTRWGULVCVULSRQFQDQVGYDDDXOTJUJOOCMWYXRASNONFESVHISQIXTLXJHIDQWTUKPSIHUCWIPBMJYWTSMCQHNPQUXTMWNGGCAQLVTIFKLUUKQNCERULFLBBJWOHLWPQXGDUBNZLZVHLLXPROMCTXFXIELPPJHHINLEQAGBZBLMPICGWOJSLQPUUCLKLSTWHGAXHGZIIKVZUXFQNOKAHZUBDINRAHNINNFWWGFGSAFMZKFMBPMIRJLURZLTGYDVOLSMRXUMZZAYLFMOXAYOLKKEJWYRWDOMOIAIHUUGVWGHCUXBXWPIIZNTXNMWQAIFLJNSDJBZFJIJEFKBDBJNDYGALSWEVHJGSYAXJBYQNGAROMUTQFHTEPVRISVFBGNTEPQPTPGGXIXNWTHMYQFEFBWPVTWYAJRGZHWSYEYWMXLIQSXQKCVQFTFAMCAMNRVOBRIBXIZJFLTXDQQOVLGAENDQRDFFXAVYTEZQMZBUKWTPPJFKULMAZPTQVYXSATSTZRLLSOHEKBUZMBLHNYJOPCGKAGECBWXAQILIYVPJYJKKKWRZWDNLFWYICCKDBIDRSQBRNQCLBMWMKPNISDUYZUGDWSIZANQVFSMTKQEMEAAPQNZKQTIRPQWOJENJREGXYSQIIWUNXUEPIDBAZKUOCQCLXSXOWDNUYDEICZVBVBQFHTGIDCYGSDTRVQGRUTNSZRCBSYCQBUVKNDSTFRBAUURPNZIJVVDUOFXJFZZHVWRKAMFHDGJZDBOQCWZXTCRJHQUNRTWMSPZSBEZELLFQOTGQRHOMJHYSYSFPOBEGRDYUJZBUKGMYCSRVZFIKOIDOAKEOOKUFPUBYWCVIJHJLCAGBHQOVYRKBDQPRCMYRIAPGCKPLUYYWAFZHXNEYGQZKGQBIEABNARTEDKQXKQTKXTRVIYTPOUZXKCHPCJEEAZJFKBFURYHPTAMCYHTNBSKNUREZAKFCKOKWRPSLPBAJCONAVGNYAZLWTSVVCDAORKMLZHWQIYBKMOLHWAHYCUVVMSQRVQFPCUADBYUJWVUIMFRKHYJJUGEHAXAWPFNSZPVANRKJNGTBNMNUMWEGEKPFHPDXVQRWFMZUELFTRYWEKJAWGGCMRURAJUZGKQDRFELLPQEIQCOALQYTXDGQXXQGSSNEKSYRYLCPCIXUKNXWDVPCAXSXVLGPDVVPPTHNFJCJUBDEOACTYSWYPQYMBEDGZZWQSDDZOHKIIONYQRROLPNDGNPHRTQSUMIMRNOFUYQCOFCFWVVILKLTXACOVSIPEQEXFSDZSVDHAFOWBJEOURHRULGPEQHKHLIOFNOZITGIZUECGLSACBRWMZOQQVBZGJNNWDMGXVOYRUCXFUXKXRGJQUAIRDJZOZMMEBSDWGBNAFLIBKSYBYIUVKCMNOODNAPRDHVBPYPPECXHMPIOQQKNCMBRAPUPSLHVSEXHCOYISYSGPAWFQGUUTWLVNHLFSUDM',3452)