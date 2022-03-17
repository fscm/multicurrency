# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Currency system.

The multicurrency module provides support for currency operations. It
supports several different currencies.

The currencies supported by this module were created with information
(alphabetic code, numeric code, and minor unit size) from ISO-4217.

.. note::
    Cryptocurrencies are not represented in the ISO-4217. Information on
    cryptocurrencies was collected on other sources.

## Supported Currencies

List of supported currencies (with the default, localized, and
international formats):

* `multicurrency.afghani.Afghani` (؋ ۱۲۳٬۴۵۶٫۷۹ | ؋ ۱۲۳٬۴۵۶٫۷۹ | AFN 123,456.79),
* `multicurrency.dinar.AlgerianDinar` (123.456,79 د.ج. | 123.456,79 د.ج. | DZD 123,456.79),
* `multicurrency.peso.ArgentinePeso` ($ 123.456,79 | AR$ 123.456,79 | ARS 123,456.79),
* `multicurrency.dram.ArmenianDram` (123 456,79 Դ | 123 456,79 Դ | AMD 123,456.79),
* `multicurrency.florin.ArubanFlorin` (ƒ123,456.79 | ƒ123,456.79 | AWG 123,456.79),
* `multicurrency.dollar.AustralianDollar` ($123,456.79 | $123,456.79 | AUD 123,456.79),
* `multicurrency.dollar.AustralianDollarAU` ($123,456.79 | AU$123,456.79 | AUD 123,456.79),
* `multicurrency.dollar.AustralianDollarCC` ($123,456.79 | CC$123,456.79 | AUD 123,456.79),
* `multicurrency.dollar.AustralianDollarKI` ($123,456.79 | KI$123,456.79 | AUD 123,456.79),
* `multicurrency.dollar.AustralianDollarMR` ($123,456.79 | NR$123,456.79 | AUD 123,456.79),
* `multicurrency.dollar.AustralianDollarTV` ($123,456.79 | TV$123,456.79 | AUD 123,456.79),
* `multicurrency.manat.AzerbaijanianManat` (123.456,79 ₼ | 123.456,79 ₼ | AZN 123,456.79),
* `multicurrency.dollar.BahamianDollar` ($123,456.79 | BS$123,456.79 | BSD 123,456.79),
* `multicurrency.dinar.BahrainiDinar` (د.ب. ١٢٣٬٤٥٦٫٧٨٩ | د.ب. ١٢٣٬٤٥٦٫٧٨٩ | BHD 123,456.789),
* `multicurrency.baht.Baht` (฿123,456.79 | ฿123,456.79 | THB 123,456.79),
* `multicurrency.balboa.Balboa` (B/. 123,456.79 | B/. 123,456.79 | PAB 123,456.79),
* `multicurrency.dollar.BarbadosDollar` ($123,456.79 | BB$123,456.79 | BBD 123,456.79),
* `multicurrency.ruble.BelarusianRuble` (123 456,79 Br | 123 456,79 Br | BYN 123,456.79),
* `multicurrency.dollar.BelizeDollar` ($123,456.79 | BZ$123,456.79 | BZD 123,456.79),
* `multicurrency.dollar.BermudianDollar` ($123,456.79 | BM$123,456.79 | BMD 123,456.79),
* `multicurrency.fuerte.BolivarFuerte` (Bs.F. 123.456,79 | Bs.F. 123.456,79 | VEF 123,456.79),
* `multicurrency.boliviano.Boliviano` (Bs. 123.456,79 | Bs. 123.456,79 | BOB 123,456.79),
* `multicurrency.real.BrazilianReal` (R$ 123.456,79 | R$ 123.456,79 | BRL 123,456.79),
* `multicurrency.dollar.BruneiDollar` ($ 123.456,79 | $ 123.456,79 | BND 123,456.79),
* `multicurrency.dollar.BruneiDollarBN` ($ 123.456,79 | BN$ 123.456,79 | BND 123,456.79),
* `multicurrency.dollar.BruneiDollarSG` ($ 123.456,79 | SG$ 123.456,79 | BND 123,456.79),
* `multicurrency.lev.BulgarianLev` (123456,79 лв. | 123456,79 лв. | BGN 123,456.79),
* `multicurrency.franc.BurundiFranc` (123 457 ₣ | 123 457 BI₣ | BIF 123,457),
* `multicurrency.franc.CFAFrancBCEAO` (123 457 ₣ | 123 457 ₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBCEAOBF` (123 457 ₣ | 123 457 BF₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBCEAOBJ` (123 457 ₣ | 123 457 BJ₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBCEAOCI` (123 457 ₣ | 123 457 CI₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBCEAOGW` (123 457 ₣ | 123 457 GW₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBCEAOML` (123 457 ₣ | 123 457 ML₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBCEAONG` (123 457 ₣ | 123 457 NG₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBCEAOSN` (123 457 ₣ | 123 457 SN₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBCEAOTG` (123 457 ₣ | 123 457 TG₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBEAC` (123 457 ₣ | 123 457 ₣ | XAF 123,457),
* `multicurrency.franc.CFAFrancBEACCD` (123 457 ₣ | 123 457 CD₣ | XAF 123,457),
* `multicurrency.franc.CFAFrancBEACCF` (123 457 ₣ | 123 457 CF₣ | XAF 123,457),
* `multicurrency.franc.CFAFrancBEACCM` (123 457 ₣ | 123 457 CM₣ | XAF 123,457),
* `multicurrency.franc.CFAFrancBEACGA` (123 457 ₣ | 123 457 GA₣ | XAF 123,457),
* `multicurrency.franc.CFAFrancBEACGQ` (123 457 ₣ | 123 457 GQ₣ | XAF 123,457),
* `multicurrency.franc.CFAFrancBEACTD` (123 457 ₣ | 123 457 TD₣ | XAF 123,457),
* `multicurrency.franc.CFPFranc` (123 457 ₣ | 123 457 ₣ | XPF 123,457),
* `multicurrency.franc.CFPFrancNC` (123 457 ₣ | 123 457 NC₣ | XPF 123,457),
* `multicurrency.franc.CFPFrancPF` (123 457 ₣ | 123 457 PF₣ | XPF 123,457),
* `multicurrency.franc.CFPFrancWF` (123 457 ₣ | 123 457 WF₣ | XPF 123,457),
* `multicurrency.dollar.CanadianDollarEN` ($123,456.79 | CA$123,456.79 | CAD 123,456.79),
* `multicurrency.dollar.CanadianDollarFR` (123 456,79 $ | 123 456,79 CA$ | CAD 123,456.79),
* `multicurrency.escudo.CapeVerdeEscudo` (123 456$79 | 123 456$79 | CVE 123,456.79),
* `multicurrency.dollar.CaymanIslandsDollar` ($123,456.79 | KY$123,456.79 | KYD 123,456.79),
* `multicurrency.cedi.Cedi` (₵123,456.79 | ₵123,456.79 | GHS 123,456.79),
* `multicurrency.peso.ChileanPeso` ($123.457 | CL$123.457 | CLP 123,457),
* `multicurrency.peso.ColombianPeso` ($ 123.456,79 | CO$ 123.456,79 | COP 123,456.79),
* `multicurrency.franc.CongoleseFranc` (123 456,79 ₣ | 123 456,79 CD₣ | CDF 123,456.79),
* `multicurrency.oro.CordobaOro` (C$123,456.79 | C$123,456.79 | NIO 123,456.79),
* `multicurrency.colon.CostaRicanColon` (₡123 456,79 | ₡123 456,79 | CRC 123,456.79),
* `multicurrency.kuna.CroatianKuna` (123.456,79 Kn | 123.456,79 Kn | HRK 123,456.79),
* `multicurrency.peso.CubanPeso` ($123,456.79 | CU$123,456.79 | CUP 123,456.79),
* `multicurrency.koruna.CzechKoruna` (123 456,79 Kč | 123 456,79 Kč | CZK 123,456.79),
* `multicurrency.dalasi.Dalasi` (D 123,456.79 | D 123,456.79 | GMD 123,456.79),
* `multicurrency.krone.DanishKrone` (123.456,79 kr | 123.456,79 kr | DKK 123,456.79),
* `multicurrency.denar.Denar` (123.456,79 ден. | 123.456,79 ден. | MKD 123,456.79),
* `multicurrency.franc.DjiboutiFranc` (123 457 ₣ | 123 457 DJ₣ | DJF 123,457),
* `multicurrency.dobra.Dobra` (123.456,79 Db | 123.456,79 Db | STN 123,456.79),
* `multicurrency.peso.DominicanPeso` ($123,456.79 | DO$123,456.79 | DOP 123,456.79),
* `multicurrency.dong.Dong` (123.457 ₫ | 123.457 ₫ | VND 123,457),
* `multicurrency.dollar.EasternCaribbeanDollar` ($123,456.79 | $123,456.79 | XCD 123,456.79),
* `multicurrency.dollar.EasternCaribbeanDollarAG` ($123,456.79 | AG$123,456.79 | XCD 123,456.79),
* `multicurrency.dollar.EasternCaribbeanDollarAI` ($123,456.79 | AI$123,456.79 | XCD 123,456.79),
* `multicurrency.dollar.EasternCaribbeanDollarDM` ($123,456.79 | DM$123,456.79 | XCD 123,456.79),
* `multicurrency.dollar.EasternCaribbeanDollarGD` ($123,456.79 | GD$123,456.79 | XCD 123,456.79),
* `multicurrency.dollar.EasternCaribbeanDollarKN` ($123,456.79 | KN$123,456.79 | XCD 123,456.79),
* `multicurrency.dollar.EasternCaribbeanDollarLC` ($123,456.79 | LC$123,456.79 | XCD 123,456.79),
* `multicurrency.dollar.EasternCaribbeanDollarMS` ($123,456.79 | MS$123,456.79 | XCD 123,456.79),
* `multicurrency.dollar.EasternCaribbeanDollarVC` ($123,456.79 | VC$123,456.79 | XCD 123,456.79),
* `multicurrency.pound.EgyptianPound` (ج.م. ١٢٣٬٤٥٦٫٧٩ | ج.م. ١٢٣٬٤٥٦٫٧٩ | EGP 123,456.79),
* `multicurrency.birr.EthiopianBirr` (ብር 123,456.79 | ብር 123,456.79 | ETB 123,456.79),
* `multicurrency.euro.Euro` (123.456,79 € | 123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroAD` (123.456,79 € | 123.456,79 AD€ | EUR 123,456.79),
* `multicurrency.euro.EuroAT` (€ 123.456,79 | AT€ 123.456,79 | EUR 123,456.79),
* `multicurrency.euro.EuroBE` (€ 123.456,79 | BE€ 123.456,79 | EUR 123,456.79),
* `multicurrency.euro.EuroCY` (123.456,79 € | 123.456,79 CY€ | EUR 123,456.79),
* `multicurrency.euro.EuroDE` (123.456,79 € | 123.456,79 DE€ | EUR 123,456.79),
* `multicurrency.euro.EuroEE` (123 456,79 € | 123 456,79 EE€ | EUR 123,456.79),
* `multicurrency.euro.EuroES` (123.456,79 € | 123.456,79 ES€ | EUR 123,456.79),
* `multicurrency.euro.EuroFI` (123 456,79 € | 123 456,79 FI€ | EUR 123,456.79),
* `multicurrency.euro.EuroFR` (123 456,79 € | 123 456,79 FR€ | EUR 123,456.79),
* `multicurrency.euro.EuroGR` (123.456,79 € | 123.456,79 GR€ | EUR 123,456.79),
* `multicurrency.euro.EuroIE` (€123,456.79 | IR€123,456.79 | EUR 123,456.79),
* `multicurrency.euro.EuroIT` (123.456,79 € | 123.456,79 IT€ | EUR 123,456.79),
* `multicurrency.euro.EuroLT` (123 456,79 € | 123 456,79 LT€ | EUR 123,456.79),
* `multicurrency.euro.EuroLU` (123.456,79 € | 123.456,79 LU€ | EUR 123,456.79),
* `multicurrency.euro.EuroLV` (123 456,79 € | 123 456,79 LV€ | EUR 123,456.79),
* `multicurrency.euro.EuroMC` (123 456,79 € | 123 456,79 MC€ | EUR 123,456.79),
* `multicurrency.euro.EuroME` (123.456,79 € | 123.456,79 ME€ | EUR 123,456.79),
* `multicurrency.euro.EuroMT` (€123,456.79 | MT€123,456.79 | EUR 123,456.79),
* `multicurrency.euro.EuroNL` (€ 123.456,79 | NL€ 123.456,79 | EUR 123,456.79),
* `multicurrency.euro.EuroPT` (€ 123.456,79 | PT€ 123.456,79 | EUR 123,456.79),
* `multicurrency.euro.EuroSBA` (123.456,79 € | 123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroSI` (123.456,79 € | 123.456,79 SI€ | EUR 123,456.79),
* `multicurrency.euro.EuroSK` (123 456,79 € | 123 456,79 SK€ | EUR 123,456.79),
* `multicurrency.euro.EuroSM` (123.456,79 € | 123.456,79 SM€ | EUR 123,456.79),
* `multicurrency.euro.EuroVA` (€123,456.79 | VA€123,456.79 | EUR 123,456.79),
* `multicurrency.euro.EuroXK` (123 456,79 € | 123 456,79 XK€ | EUR 123,456.79),
* `multicurrency.pound.FalklandIslandsPound` (£123,456.79 | FK£123,456.79 | FKP 123,456.79),
* `multicurrency.dollar.FijiDollar` ($123,456.79 | FJ$123,456.79 | FJD 123,456.79),
* `multicurrency.forint.Forint` (123 457 Ft | 123 457 Ft | HUF 123,457),
* `multicurrency.pound.GibraltarPound` (£123,456.79 | GI£123,456.79 | GIP 123,456.79),
* `multicurrency.gourde.Gourde` (G 123,456.79 | G 123,456.79 | HTG 123,456.79),
* `multicurrency.guarani.Guarani` (₲ 123.457 | ₲ 123.457 | PYG 123,457),
* `multicurrency.franc.GuineaFranc` (123 457 ₣ | 123 457 GN₣ | GNF 123,457),
* `multicurrency.dollar.GuyanaDollar` ($123,456.79 | GY$123,456.79 | GYD 123,456.79),
* `multicurrency.dollar.HongKongDollar` ($123,456.79 | HK$123,456.79 | HKD 123,456.79),
* `multicurrency.hryvnia.Hryvnia` (123 456,79 ₴ | 123 456,79 ₴ | UAH 123,456.79),
* `multicurrency.krona.IcelandKrona` (123.457 Kr | 123.457 Kr | ISK 123,457),
* `multicurrency.rupee.IndianRupee` (₹123,456.79 | ₹123,456.79 | INR 123,456.79),
* `multicurrency.rupee.IndianRupeeBT` (₹123,456.79 | BT₹123,456.79 | INR 123,456.79),
* `multicurrency.rupee.IndianRupeeIN` (₹123,456.79 | IN₹123,456.79 | INR 123,456.79),
* `multicurrency.rial.IranianRial` (۱۲۳٬۴۵۶٫۷۹ ﷼ | ۱۲۳٬۴۵۶٫۷۹ ﷼ | IRR 123,456.79),
* `multicurrency.dinar.IraqiDinar` (د.ع. ١٢٣٬٤٥٦٫٧٨٩ | د.ع. ١٢٣٬٤٥٦٫٧٨٩ | IQD 123,456.789),
* `multicurrency.dollar.JamaicanDollar` ($123,456.79 | JM$123,456.79 | JMD 123,456.79),
* `multicurrency.dinar.JordanianDinar` (د.أ. ١٢٣٬٤٥٦٫٧٨٩ | د.أ. ١٢٣٬٤٥٦٫٧٨٩ | JOD 123,456.789),
* `multicurrency.shilling.KenyanShilling` (Ksh 123,456.79 | Ksh 123,456.79 | KES 123,456.79),
* `multicurrency.kina.Kina` (K 123,456.79 | K 123,456.79 | PGK 123,456.79),
* `multicurrency.kip.Kip` (₭123.456,79 | ₭123.456,79 | LAK 123,456.79),
* `multicurrency.marka.KonvertibilnaMarka` (123,456.79 КМ | 123,456.79 КМ | BAM 123,456.79),
* `multicurrency.dinar.KuwaitiDinar` (د.ك. ١٢٣٬٤٥٦٫٧٨٩ | د.ك. ١٢٣٬٤٥٦٫٧٨٩ | KWD 123,456.789),
* `multicurrency.kwacha.Kwacha` (MK 123,456.79 | MK 123,456.79 | MWK 123,456.79),
* `multicurrency.kwanza.Kwanza` (123 456,79 Kz | 123 456,79 Kz | AOA 123,456.79),
* `multicurrency.kyat.Kyat` (၁၂၃,၄၅၆.၇၉ K | ၁၂၃,၄၅၆.၇၉ K | MMK 123,456.79),
* `multicurrency.lari.Lari` (123 456,79 ლ | 123 456,79 GEლ | GEL 123,456.79),
* `multicurrency.pound.LebanesePound` (ل.ل. ١٢٣٬٤٥٧ | ل.ل. ١٢٣٬٤٥٧ | LBP 123,457),
* `multicurrency.lek.Lek` (123 456,79 Lek | 123 456,79 Lek | ALL 123,456.79),
* `multicurrency.lempira.Lempira` (L 123,456.79 | L 123,456.79 | HNL 123,456.79),
* `multicurrency.leone.Leone` (Le 123,456.79 | Le 123,456.79 | SLL 123,456.79),
* `multicurrency.leu.Leu` (123.456,79 L | 123.456,79 L | RON 123,456.79),
* `multicurrency.dollar.LiberianDollar` ($123,456.79 | LR$123,456.79 | LRD 123,456.79),
* `multicurrency.dinar.LibyanDinar` (د.ل. 123.456,789 | د.ل. 123.456,789 | LYD 123,456.789),
* `multicurrency.lilangeni.Lilangeni` (L 123,456.79 | L 123,456.79 | SZL 123,456.79),
* `multicurrency.loti.Loti` (L 123,456.79 | L 123,456.79 | LSL 123,456.79),
* `multicurrency.ariary.MalagasyAriary` (123 457 Ar | 123 457 Ar | MGA 123,457),
* `multicurrency.ringgit.MalaysianRinggit` (RM 123,456.79 | RM 123,456.79 | MYR 123,456.79),
* `multicurrency.manat.Manat` (123 456,79 m | 123 456,79 m | TMT 123,456.79),
* `multicurrency.rupee.MauritiusRupee` (₨ 123,456.79 | ₨ 123,456.79 | MUR 123,456.79),
* `multicurrency.metical.Metical` (123.457 MTn | 123.457 MTn | MZN 123,457),
* `multicurrency.peso.MexicanPeso` ($123,456.79 | MX$123,456.79 | MXN 123,456.79),
* `multicurrency.leu.MoldovanLeu` (123.456,79 L | 123.456,79 L | MDL 123,456.79),
* `multicurrency.dirham.MoroccanDirham` (د.م. ١٢٣٬٤٥٦٫٧٩ | د.م. ١٢٣٬٤٥٦٫٧٩ | MAD 123,456.79),
* `multicurrency.naira.Naira` (₦123,456.79 | ₦123,456.79 | NGN 123,456.79),
* `multicurrency.nakfa.Nakfa` (Nfk 123,456.79 | Nfk 123,456.79 | ERN 123,456.79),
* `multicurrency.dollar.NamibiaDollar` ($123,456.79 | NA$123,456.79 | NAD 123,456.79),
* `multicurrency.rupee.NepaleseRupee` (नेरू १२३,४५६.७९ | नेरू १२३,४५६.७९ | NPR 123,456.79),
* `multicurrency.shekel.NewIsraeliShekel` (123,456.79 ₪ | 123,456.79 ₪ | ILS 123,456.79),
* `multicurrency.shekel.NewIsraeliShekelIL` (123,456.79 ₪ | 123,456.79 IL₪ | ILS 123,456.79),
* `multicurrency.shekel.NewIsraeliShekelPS` (123,456.79 ₪ | 123,456.79 PS₪ | ILS 123,456.79),
* `multicurrency.dollar.NewZealandDollar` ($123,456.79 | $123,456.79 | NZD 123,456.79),
* `multicurrency.dollar.NewZealandDollarCK` ($123,456.79 | CK$123,456.79 | NZD 123,456.79),
* `multicurrency.dollar.NewZealandDollarNU` ($123,456.79 | NU$123,456.79 | NZD 123,456.79),
* `multicurrency.dollar.NewZealandDollarNZ` ($123,456.79 | NZ$123,456.79 | NZD 123,456.79),
* `multicurrency.dollar.NewZealandDollarPN` ($123,456.79 | PN$123,456.79 | NZD 123,456.79),
* `multicurrency.ngultrum.Ngultrum` (Nu. ༡༢༣,༤༥༦.༧༩ | Nu. ༡༢༣,༤༥༦.༧༩ | BTN 123,456.79),
* `multicurrency.won.NorthKoreanWon` (₩ 123,456.79 | ₩ 123,456.79 | KPW 123,456.79),
* `multicurrency.krone.NorwegianKrone` (kr 123 456,79 | kr 123 456,79 | NOK 123,456.79),
* `multicurrency.nuevo_sol.NuevoSol` (S/. 123,456.79 | S/. 123,456.79 | PEN 123,456.79),
* `multicurrency.ouguiya.Ouguiya` (١٢٣٬٤٥٦٫٧٩ أ.م | ١٢٣٬٤٥٦٫٧٩ أ.م | MRU 123,456.79),
* `multicurrency.pzloty.PZloty` (123 456,79 zł | 123 456,79 zł | PLN 123,456.79),
* `multicurrency.paanga.Paanga` (T$ 123,456.79 | T$ 123,456.79 | TOP 123,456.79),
* `multicurrency.rupee.PakistanRupee` (₨ 123,456.79 | ₨ 123,456.79 | PKR 123,456.79),
* `multicurrency.pataca.Pataca` (P 123,456.79 | P 123,456.79 | MOP 123,456.79),
* `multicurrency.peso.PesoUruguayo` ($ 123.456,79 | UY$ 123.456,79 | UYU 123,456.79),
* `multicurrency.peso.PhilippinePeso` (₱123,456.79 | ₱123,456.79 | PHP 123,456.79),
* `multicurrency.pound.PoundSterling` (£123,456.79 | £123,456.79 | GBP 123,456.79),
* `multicurrency.pound.PoundSterlingGB` (£123,456.79 | GB£123,456.79 | GBP 123,456.79),
* `multicurrency.pound.PoundSterlingGG` (£123,456.79 | GG£123,456.79 | GBP 123,456.79),
* `multicurrency.pound.PoundSterlingIM` (£123,456.79 | IM£123,456.79 | GBP 123,456.79),
* `multicurrency.pound.PoundSterlingIO` (£123,456.79 | IO£123,456.79 | GBP 123,456.79),
* `multicurrency.pula.Pula` (P 123,456.79 | P 123,456.79 | BWP 123,456.79),
* `multicurrency.rial.QatariRial` (ر.ق. ١٢٣٬٤٥٦٫٧٩ | ر.ق. ١٢٣٬٤٥٦٫٧٩ | QAR 123,456.79),
* `multicurrency.quetzal.Quetzal` (Q 123,456.79 | Q 123,456.79 | GTQ 123,456.79),
* `multicurrency.rand.Rand` (R 123 456.79 | R 123 456.79 | ZAR 123,456.79),
* `multicurrency.rand.RandLS` (R 123,456.79 | LSR 123,456.79 | ZAR 123,456.79),
* `multicurrency.rand.RandNA` (R 123 456.79 | NAR 123 456.79 | ZAR 123,456.79),
* `multicurrency.rand.RandZA` (R 123 456.79 | ZAR 123 456.79 | ZAR 123,456.79),
* `multicurrency.rial.RialOmani` (ر.ع. ١٢٣٬٤٥٦٫٧٨٩ | ر.ع. ١٢٣٬٤٥٦٫٧٨٩ | OMR 123,456.789),
* `multicurrency.riel.Riel` (123.456,79៛ | 123.456,79៛ | KHR 123,456.79),
* `multicurrency.rufiyaa.Rufiyaa` (ރ. 123,456.79 | ރ. 123,456.79 | MVR 123,456.79),
* `multicurrency.rupiah.Rupiah` (Rp 123.456,79 | Rp 123.456,79 | IDR 123,456.79),
* `multicurrency.ruble.RussianRuble` (123 456,79 ₽ | 123 456,79 ₽ | RUB 123,456.79),
* `multicurrency.ruble.RussianRubleGE` (123 456,79 ₽ | 123 456,79 GE₽ | RUB 123,456.79),
* `multicurrency.ruble.RussianRubleRU` (123 456,79 ₽ | 123 456,79 RU₽ | RUB 123,456.79),
* `multicurrency.franc.RwandaFranc` (₣ 123.457 | RW₣ 123.457 | RWF 123,457),
* `multicurrency.pound.SaintHelenaPound` (£123,456.79 | SH£123,456.79 | SHP 123,456.79),
* `multicurrency.riyal.SaudiRiyal` (ر.س. ١٢٣٬٤٥٦٫٧٩ | ر.س. ١٢٣٬٤٥٦٫٧٩ | SAR 123,456.79),
* `multicurrency.dinar.SerbianDinarSR` (123 456,79 дин. | 123 456,79 дин. | RSD 123,456.79),
* `multicurrency.dinar.SerbianDinarXK` (123.456,79 дин. | 123.456,79 дин. | RSD 123,456.79),
* `multicurrency.rupee.SeychellesRupee` (₨ 123,456.79 | ₨ 123,456.79 | SCR 123,456.79),
* `multicurrency.dollar.SingaporeDollar` ($123,456.79 | $123,456.79 | SGD 123,456.79),
* `multicurrency.dollar.SingaporeDollarBN` ($123,456.79 | BN$123,456.79 | SGD 123,456.79),
* `multicurrency.dollar.SingaporeDollarSG` ($123,456.79 | SG$123,456.79 | SGD 123,456.79),
* `multicurrency.dollar.SolomonIslandsDollar` ($123,456.79 | SB$123,456.79 | SBD 123,456.79),
* `multicurrency.som.Som` (123 456,79 Лв | 123 456,79 Лв | KGS 123,456.79),
* `multicurrency.shilling.SomaliShilling` (SSh 123,456.79 | SSh 123,456.79 | SOS 123,456.79),
* `multicurrency.somoni.Somoni` (ЅМ 123,456.79 | ЅМ 123,456.79 | TJS 123,456.79),
* `multicurrency.won.SouthKoreanWon` (₩123,457 | ₩123,457 | KRW 123,457),
* `multicurrency.rupee.SriLankaRupee` (රු. 123,456.79 | රු. 123,456.79 | LKR 123,456.79),
* `multicurrency.pound.SudanesePound` (١٢٣٬٤٥٦٫٧٩ ج.س | ١٢٣٬٤٥٦٫٧٩ ج.س | SDG 123,456.79),
* `multicurrency.dollar.SurinameDollar` ($ 123.456,79 | SR$ 123.456,79 | SRD 123,456.79),
* `multicurrency.krona.SwedishKrona` (123 456,79 kr | 123 456,79 kr | SEK 123,456.79),
* `multicurrency.franc.SwissFranc` (₣ 123'456.79 | ₣ 123'456.79 | CHF 123,456.79),
* `multicurrency.franc.SwissFrancCH` (₣ 123'456.79 | CH₣ 123'456.79 | CHF 123,456.79),
* `multicurrency.franc.SwissFrancLI` (₣ 123'456.79 | LI₣ 123'456.79 | CHF 123,456.79),
* `multicurrency.pound.SyrianPound` (١٢٣٬٤٥٦٫٧٩ ل.س | ١٢٣٬٤٥٦٫٧٩ ل.س | SYP 123,456.79),
* `multicurrency.dollar.TaiwanDollar` ($123,456.79 | TW$123,456.79 | TWD 123,456.79),
* `multicurrency.taka.Taka` (১২৩,৪৫৬.৭৯৳ | ১২৩,৪৫৬.৭৯৳ | BDT 123,456.79),
* `multicurrency.tala.Tala` (T 123,456.79 | T 123,456.79 | WST 123,456.79),
* `multicurrency.shilling.TanzanianShilling` (TSh 123,456.79 | TSh 123,456.79 | TZS 123,456.79),
* `multicurrency.tenge.Tenge` (123 456,79 〒 | 123 456,79 〒 | KZT 123,456.79),
* `multicurrency.dollar.TrinidadandTobagoDollar` ($123,456.79 | TT$123,456.79 | TTD 123,456.79),
* `multicurrency.tugrik.Tugrik` (₮ 123,456.79 | ₮ 123,456.79 | MNT 123,456.79),
* `multicurrency.dinar.TunisianDinar` (د.ت. 123.456,789 | د.ت. 123.456,789 | TND 123,456.789),
* `multicurrency.lira.TurkishLira` (₤123.456,79 | ₤123.456,79 | TRY 123,456.79),
* `multicurrency.lira.TurkishLiraCY` (₤123.456,79 | CY₤123.456,79 | TRY 123,456.79),
* `multicurrency.lira.TurkishLiraTR` (₤123.456,79 | TR₤123.456,79 | TRY 123,456.79),
* `multicurrency.dirham.UAEDirham` (د.إ. ١٢٣٬٤٥٦٫٧٩ | د.إ. ١٢٣٬٤٥٦٫٧٩ | AED 123,456.79),
* `multicurrency.dollar.USDollar` ($123,456.79 | US$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarAS` ($123,456.79 | AS$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarFM` ($123,456.79 | FM$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarGU` ($123,456.79 | GU$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarHT` ($123,456.79 | HT$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarIO` ($123,456.79 | IO$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarMH` ($123,456.79 | MH$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarMP` ($123,456.79 | MP$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarPA` ($123,456.79 | PA$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarPC` ($123,456.79 | PC$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarPR` ($123,456.79 | PR$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarPW` ($123,456.79 | PW$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarTC` ($123,456.79 | TC$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarVG` ($123,456.79 | VG$123,456.79 | USD 123,456.79),
* `multicurrency.dollar.USDollarVI` ($123,456.79 | VI$123,456.79 | USD 123,456.79),
* `multicurrency.shilling.UgandaShilling` (USh 123,457 | USh 123,457 | UGX 123,457),
* `multicurrency.sum.UzbekistanSum` (123 456,79 сўм | 123 456,79 сўм | UZS 123,456.79),
* `multicurrency.vatu.Vatu` (Vt 123,457 | Vt 123,457 | VUV 123,457),
* `multicurrency.rial.YemeniRial` (١٢٣٬٤٥٦٫٧٩ ﷼ | ١٢٣٬٤٥٦٫٧٩ ﷼ | YER 123,456.79),
* `multicurrency.yen.Yen` (¥123,457 | ¥123,457 | JPY 123,457),
* `multicurrency.yuan.Yuan` (¥123,456.79 | ¥123,456.79 | CNY 123,456.79),
* `multicurrency.kwacha.ZambianKwacha` (ZK 123,456.79 | ZK 123,456.79 | ZMW 123,456.79),
* `multicurrency.dollar.ZimbabweDollar` ($ 123,456.79 | ZW$ 123,456.79 | ZWL 123,456.79)

List of supported cryptocurrencies (with the default, localized, and
international formats):

* `multicurrency.crypto.Bitcoin` (₿123,456.78900000 | ₿123,456.78900000 | XBT 123,456.78900000),
* `multicurrency.crypto.EOS` (ε123,456.7890 | ε123,456.7890 | EOS 123,456.7890),
* `multicurrency.crypto.Ethereum` (Ξ123,456.789000000000000000 | Ξ123,456.789000000000000000 | ETH 123,456.789000000000000000),
* `multicurrency.crypto.Monero` (ɱ123,456.789000000000 | ɱ123,456.789000000000 | XMR 123,456.789000000000),
* `multicurrency.crypto.Ripple` (✕123,456.789000 | ✕123,456.789000 | XRP 123,456.789000),
* `multicurrency.crypto.StellarLumens` (*123,456.7890000 | *123,456.7890000 | XLM 123,456.7890000),
* `multicurrency.crypto.Tezos` (ꜩ123,456.789000 | ꜩ123,456.789000 | XTZ 123,456.789000),
* `multicurrency.crypto.Zcash` (ⓩ123,456.78900000 | ⓩ123,456.78900000 | ZEC 123,456.78900000)

## Usage

Simple usage example:

    >>> from multicurrency import Euro
    >>> euro = Euro(1000)
    >>> print(euro)
    1.000,00 €
    >>> print(euro + Euro(0.50))
    1.000,50 €

Unsupported currencies can be represented by creating a generic
`multicurrency._currency.Currency` object with the desired settings.

    >>> from multicurrency import Currency
    >>> bitcoin = Currency(
    ...     amount=1000,
    ...     alpha_code='XBT',
    ...     numeric_code='0',
    ...     symbol='₿',
    ...     symbol_ahead=True,
    ...     symbol_separator='',
    ...     decimal_places=8,
    ...     decimal_sign='.',
    ...     grouping_sign=',')
    >>> print(bitcoin)
    ₿1,000.00000000

To help working with unsupported currencies the settings can be defined
in a dictionary and used when needed:

    >>> from multicurrency import Currency
    >>> settings = {
    ...     'alpha_code':'XBT',
    ...     'numeric_code':'0',
    ...     'symbol':'₿',
    ...     'symbol_ahead':True,
    ...     'symbol_separator':'',
    ...     'decimal_places':8,
    ...     'decimal_sign':'.',
    ...     'grouping_sign':','}
    >>> bitcoin = Currency(1000, **settings)
    >>> print(bitcoin)
    ₿1,000.00000000

Currencies can also be represented with the ISO 4217 three-letter code
instead of the `symbol`.

    >>> from multicurrency import Euro
    >>> euro = Euro(1000, international=True)
    >>> print(euro)
    EUR 1,000.00

## Localization

The multicurrency library allows you to obtain a localized version of the
currency representation:

    >>> from multicurrency import TaiwanDollar, USDollar
    >>> tw_dollar = TaiwanDollar('27.65')
    >>> us_dollar = USDollar('1')
    >>> print(us_dollar.localized(), '=', tw_dollar.localized())
    US$1.00 = TW$27.65

## Precision

The multicurrency library has a user alterable precision (defaulting to
28 places) which can be as large as needed for a given problem:

    >>> from multicurrency import CurrencyContext, Euro
    >>> for precision in [1, 2, 3, 4, 5, 6]:
    ...     CurrencyContext.prec = precision
    ...     result = Euro(1) / 7
    ...     print(result.precision(precision))
    0,1 €
    0,14 €
    0,143 €
    0,1429 €
    0,14286 €
    0,142857 €

It also has a user alterable rounding method (defaulting to
ROUND_HALF_EVEN) which can be changed as needed:

    >>> from multicurrency import CurrencyContext, Euro
    >>> CurrencyContext.prec = 4
    >>> for rounding in [
    ...         'ROUND_CEILING',
    ...         'ROUND_DOWN',
    ...         'ROUND_FLOOR',
    ...         'ROUND_HALF_DOWN',
    ...         'ROUND_HALF_EVEN',
    ...         'ROUND_HALF_UP',
    ...         'ROUND_UP',
    ...         'ROUND_05UP']:
    ...     CurrencyContext.rounding = rounding
    ...     result = Euro(1) / 7
    ...     print(f'{rounding:16}', result.precision(4))
    ROUND_CEILING    0,1429 €
    ROUND_DOWN       0,1428 €
    ROUND_FLOOR      0,1428 €
    ROUND_HALF_DOWN  0,1429 €
    ROUND_HALF_EVEN  0,1429 €
    ROUND_HALF_UP    0,1429 €
    ROUND_UP         0,1429 €
    ROUND_05UP       0,1428 €

Default values can be restored with:

    >>> from multicurrency import (
    ...     CurrencyContext,
    ...     DEFAULT_PRECISION,
    ...     DEFAULT_ROUNDING)
    >>> CurrencyContext.prec = DEFAULT_PRECISION
    >>> CurrencyContext.rounding = DEFAULT_ROUNDING
    >>> print(CurrencyContext.prec, CurrencyContext.rounding)
    28 ROUND_HALF_EVEN

Supported rounding methods are described on the
`multicurrency._currency.CurrencyContext` class.

## Formatting

The `multicurrency._currency.Currency` class allows you to create
and customize your own value formatting behaviors using the same
implementation as the built-in `format()` method.

The specification for the formatting feature is as follows:

    [dp][ds][gs][gp][spec]

The meaning of the various alignment options is as follows:

| Option | Type   | Meaning                                                                               |
|:-------|:-------|:--------------------------------------------------------------------------------------|
| [dp]   | int+   | The number of decimal places (integer number with one or more digits).                |
| [ds]   | str{1} | The decimal sign (single non-digit character).                                        |
| [gs]   | str{1} | The grouping sign (single non-digit character).                                       |
| [gp]   | int+   | The number of digits to group the number by (integer number with one or more digits). |
| [spec] | str    | The formatting spec (a strig with the order of currency parts).                       |

All fields are optional although for the first four fields when setting
one the fields on the left of that are required to be set as well.

The available string currency parts for `[spec]` are:

| Part | Meaning                                                                                                                     |
|:-----|:----------------------------------------------------------------------------------------------------------------------------|
| %a   | The currency's amount as seen in the default representation of the currency (the numeral system of the currency's country). |
| %A   | The currency's amount in (western) arabic numerals.                                                                         |
| %c   | The currency's alpha code (as seen on the international representation of the currency).                                    |
| %s   | The currency's symbol.                                                                                                      |
| %S   | The currency's localized symbol.                                                                                            |
| %_   | The currency's symbol separator.                                                                                            |

Basic examples of how to use the `multicurrency._currency.Currency`
formatting feature:

    Using the built-in `format()` method

        >>> from multicurrency import Euro
        >>> euro = Euro(1000000*(1/7))
        >>> format(euro, '4%a')
        '142.857,1429'

    Using the `'new' string` formating method

        >>> from multicurrency import Euro
        >>> euro = Euro(1000000*(1/7))
        >>> '{:4%a}'.format(euro)
        '142.857,1429'

    Using the `f-string` method

        >>> from multicurrency import Euro
        >>> euro = Euro(1000000*(1/7))
        >>> f'{euro:4%a}'
        '142.857,1429'

Some more examples of the `multicurrency._currency.Currency` formatting
feature usage (using the `f-string` method):

    >>> from multicurrency import Euro
    >>> euro = Euro(1000000*(1/7))
    >>> print(euro)
    142.857,14 €

    >>> print(f'{euro}')
    142.857,14 €

    >>> print(f'{euro:_}')
    142.857_14 €

    >>> print(f'{euro:.,}')
    142,857.14 €

    >>> print(f'{euro:3.,}')
    142,857.143 €

    >>> print(f'{euro:3.,2}')
    14,28,57.143 €

    >>> print(f'{euro:_2}')
    14.28.57_14 €

    >>> print(f'{euro:.,2}')
    14,28,57.14 €

    >>> print(f'{euro:3%a}')
    142.857,143

    >>> print(f'{euro:3_%a}')
    142.857_143

    >>> print(f'{euro:3#_%a}')
    142_857#143

    >>> print(f'{euro:3.,2%a}')
    14,28,57.143

    >>> print(f'{euro:3.,4%a}')
    14,2857.143

    >>> print(f'{euro:.,4%a}')
    14,2857.14

    >>> print(f'{euro:%a}')
    142.857,14

    >>> print(f'{euro:%a%_%c}')
    142.857,14 EUR

    >>> print(f'{euro:%a %c}')
    142.857,14 EUR

## Operations

Several operations are supported by the several library classes.

* Absolute

    Produces the absolute value of a given currency.

        >>> from multicurrency import Euro
        >>> euro = abs(Euro(-2))
        >>> print(euro)
        2,00 €

* Addiction

    Addiction is supported only between currencies of the same type.

        >>> from multicurrency import Euro
        >>> euro1 = Euro(2.5)
        >>> euro2 = Euro(3)
        >>> print(euro1 + euro2)
        5,50 €

* Boolean

    Produces 'True' for values of currency other than zero. 'False'
    otherwise.

        >>> from multicurrency import Euro
        >>> bool(Euro(0))
        False
        >>> bool(Euro(1))
        True

* Ceiling

    Produces a new currency rounded up to the nearest integer.

        >>> from multicurrency import Euro
        >>> from math import ceil
        >>> print(ceil(Euro(1/7)))
        1,00 €

* Copy

    Produces a copy of itself.

        >>> from multicurrency import Euro
        >>> from copy import copy
        >>> euro = copy(Euro(1/7))
        >>> print(euro)
        0,14 €

* Division

    Produces a new currency with the value of the division of the
    currency by either an `int`, `float`, or `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> euro = Euro(7) / 2
        >>> print(euro)
        3,50 €

* Divmod

    Produces a tuple consisting of the currencies with the quotient and
    the remainder of the division of the currency by either an `int`,
    `float`, or `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> q, r = divmod(Euro(7), 2)
        >>> print(q, r)
        3,00 € 1,00 €

* Float

    Produces a `float` with the value of the currency amount.

        >>> from multicurrency import Euro
        >>> float(Euro(1/7))
        0.14285714285714285

* Flooring

    Produces a new currency rounded down to the nearest integer.

        >>> from multicurrency import Euro
        >>> from math import floor
        >>> print(floor(Euro(7/2)))
        3,00 €

* Floordiv

    Produces a new currency with the integral part of the quotient of
    the division of the currency by either an `int`, `float`, or
    `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> q = Euro(7) // 2
        >>> print(q)
        3,00 €

* Hash

    Produces a hash representation of the
    `multicurrency._currency.Currency`.

        >>> from multicurrency import Euro
        >>> hash(Euro(7)) # doctest: +SKIP
        1166476495300974230

* Int

    Produces an `int` with the value of the currency amount.

        >>> from multicurrency import Euro
        >>> int(Euro(7/2))
        3

* Mod

    Produces a new currency with the value of the remainder of the
    division of the currency by either an `int`, `float`, or
    `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> r = Euro(7) % 2
        >>> print(r)
        1,00 €

* Multiplication

    Multiplication is supported only between a currency and an `int`,
    `float`, or `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> print(Euro(2) * 2.5)
        5,00 €

* Round

    Produces a new currency with the amount of the currency rounded to
    a given precision.

        >>> from multicurrency import Euro
        >>> r = round(Euro(1/7), 3)
        >>> print(r.amount)
        0.143

* Subtraction

    Subtraction is supported only between currencies of the same type.

        >>> from multicurrency import Euro
        >>> euro1 = Euro(2)
        >>> euro2 = Euro(3)
        >>> print(euro1 - euro2)
        -1,00 €

* Other Operations

    This library also supports the basic comparison operations between
    two objects of the same currency.

        >>> from multicurrency import Euro
        >>> euro1 = Euro(2)
        >>> euro2 = Euro(3)
        >>> euro1 > euro2
        False
        >>> euro1 >= euro2
        False
        >>> euro1 < euro2
        True
        >>> euro1 <= euro2
        True
        >>> euro1 == euro2
        False
        >>> euro1 != euro2
        True
"""  # pylint: disable=line-too-long  # noqa: E501,W505

from ._currency import (
    Currency,
    CurrencyContext,
    DEFAULT_PRECISION,
    DEFAULT_ROUNDING)
from ._exceptions import (
    CurrencyException,
    CurrencyInvalidDivision,
    CurrencyInvalidMultiplication,
    CurrencyInvalidOperation,
    CurrencyMismatchException,
    CurrencyTypeException)
from .afghani import Afghani
from .ariary import MalagasyAriary
from .baht import Baht
from .balboa import Balboa
from .birr import EthiopianBirr
from .boliviano import Boliviano
from .cedi import Cedi
from .colon import CostaRicanColon
from .crypto import (
    EOS,
    Ethereum,
    Bitcoin,
    StellarLumens,
    Monero,
    Ripple,
    Tezos,
    Zcash)
from .dalasi import Dalasi
from .denar import Denar
from .dinar import (
    BahrainiDinar,
    AlgerianDinar,
    IraqiDinar,
    JordanianDinar,
    KuwaitiDinar,
    LibyanDinar,
    SerbianDinarXK,
    SerbianDinarSR,
    TunisianDinar)
from .dirham import (
    UAEDirham,
    MoroccanDirham)
from .dobra import Dobra
from .dollar import (
    AustralianDollar,
    AustralianDollarAU,
    AustralianDollarKI,
    AustralianDollarCC,
    AustralianDollarMR,
    AustralianDollarTV,
    BarbadosDollar,
    BermudianDollar,
    BruneiDollar,
    BruneiDollarBN,
    BruneiDollarSG,
    BahamianDollar,
    BelizeDollar,
    CanadianDollarEN,
    CanadianDollarFR,
    FijiDollar,
    GuyanaDollar,
    HongKongDollar,
    JamaicanDollar,
    CaymanIslandsDollar,
    LiberianDollar,
    NamibiaDollar,
    NewZealandDollar,
    NewZealandDollarCK,
    NewZealandDollarNZ,
    NewZealandDollarNU,
    NewZealandDollarPN,
    SolomonIslandsDollar,
    SingaporeDollar,
    SingaporeDollarBN,
    SingaporeDollarSG,
    SurinameDollar,
    TrinidadandTobagoDollar,
    TaiwanDollar,
    USDollar,
    USDollarAS,
    USDollarIO,
    USDollarVG,
    USDollarGU,
    USDollarHT,
    USDollarMH,
    USDollarFM,
    USDollarMP,
    USDollarPC,
    USDollarPW,
    USDollarPA,
    USDollarPR,
    USDollarTC,
    USDollarVI,
    EasternCaribbeanDollar,
    EasternCaribbeanDollarAI,
    EasternCaribbeanDollarAG,
    EasternCaribbeanDollarDM,
    EasternCaribbeanDollarGD,
    EasternCaribbeanDollarMS,
    EasternCaribbeanDollarKN,
    EasternCaribbeanDollarLC,
    EasternCaribbeanDollarVC,
    ZimbabweDollar)
from .dong import Dong
from .dram import ArmenianDram
from .escudo import CapeVerdeEscudo
from .euro import (
    Euro,
    EuroSBA,
    EuroAD,
    EuroAT,
    EuroBE,
    EuroCY,
    EuroEE,
    EuroFI,
    EuroFR,
    EuroDE,
    EuroGR,
    EuroIE,
    EuroIT,
    EuroXK,
    EuroLV,
    EuroLT,
    EuroLU,
    EuroMT,
    EuroMC,
    EuroME,
    EuroNL,
    EuroPT,
    EuroSM,
    EuroSK,
    EuroSI,
    EuroES,
    EuroVA)
from .florin import ArubanFlorin
from .forint import Forint
from .franc import (
    BurundiFranc,
    CongoleseFranc,
    SwissFranc,
    SwissFrancLI,
    SwissFrancCH,
    DjiboutiFranc,
    GuineaFranc,
    RwandaFranc,
    CFAFrancBEAC,
    CFAFrancBEACCM,
    CFAFrancBEACCF,
    CFAFrancBEACTD,
    CFAFrancBEACCD,
    CFAFrancBEACGQ,
    CFAFrancBEACGA,
    CFAFrancBCEAO,
    CFAFrancBCEAOBJ,
    CFAFrancBCEAOBF,
    CFAFrancBCEAOCI,
    CFAFrancBCEAOGW,
    CFAFrancBCEAOML,
    CFAFrancBCEAONG,
    CFAFrancBCEAOSN,
    CFAFrancBCEAOTG,
    CFPFranc,
    CFPFrancPF,
    CFPFrancNC,
    CFPFrancWF)
from .fuerte import BolivarFuerte
from .gourde import Gourde
from .guarani import Guarani
from .hryvnia import Hryvnia
from .kina import Kina
from .kip import Kip
from .koruna import CzechKoruna
from .krona import (
    IcelandKrona,
    SwedishKrona)
from .krone import (
    DanishKrone,
    NorwegianKrone)
from .kuna import CroatianKuna
from .kwacha import (
    Kwacha,
    ZambianKwacha)
from .kwanza import Kwanza
from .kyat import Kyat
from .lari import Lari
from .lek import Lek
from .lempira import Lempira
from .leone import Leone
from .leu import (
    MoldovanLeu,
    Leu)
from .lev import BulgarianLev
from .lilangeni import Lilangeni
from .lira import (
    TurkishLira,
    TurkishLiraCY,
    TurkishLiraTR)
from .loti import Loti
from .manat import (
    AzerbaijanianManat,
    Manat)
from .marka import KonvertibilnaMarka
from .metical import Metical
from .naira import Naira
from .nakfa import Nakfa
from .ngultrum import Ngultrum
from .nuevo_sol import NuevoSol
from .oro import CordobaOro
from .ouguiya import Ouguiya
from .paanga import Paanga
from .pataca import Pataca
from .peso import (
    ArgentinePeso,
    ChileanPeso,
    ColombianPeso,
    CubanPeso,
    DominicanPeso,
    MexicanPeso,
    PhilippinePeso,
    PesoUruguayo)
from .pound import (
    EgyptianPound,
    FalklandIslandsPound,
    PoundSterling,
    PoundSterlingGG,
    PoundSterlingIO,
    PoundSterlingGB,
    PoundSterlingIM,
    GibraltarPound,
    LebanesePound,
    SudanesePound,
    SaintHelenaPound,
    SyrianPound)
from .pula import Pula
from .pzloty import PZloty
from .quetzal import Quetzal
from .rand import (
    Rand,
    RandLS,
    RandNA,
    RandZA)
from .real import BrazilianReal
from .rial import (
    IranianRial,
    RialOmani,
    QatariRial,
    YemeniRial)
from .riel import Riel
from .ringgit import MalaysianRinggit
from .riyal import SaudiRiyal
from .ruble import (
    BelarusianRuble,
    RussianRuble,
    RussianRubleRU,
    RussianRubleGE)
from .rufiyaa import Rufiyaa
from .rupee import (
    IndianRupee,
    IndianRupeeBT,
    IndianRupeeIN,
    SriLankaRupee,
    MauritiusRupee,
    NepaleseRupee,
    PakistanRupee,
    SeychellesRupee)
from .rupiah import Rupiah
from .shekel import (
    NewIsraeliShekel,
    NewIsraeliShekelIL,
    NewIsraeliShekelPS)
from .shilling import (
    KenyanShilling,
    SomaliShilling,
    TanzanianShilling,
    UgandaShilling)
from .som import Som
from .somoni import Somoni
from .sum import UzbekistanSum
from .taka import Taka
from .tala import Tala
from .tenge import Tenge
from .tugrik import Tugrik
from .vatu import Vatu
from .won import (
    NorthKoreanWon,
    SouthKoreanWon)
from .yen import Yen
from .yuan import Yuan


__all__ = [
    'Currency',
    'CurrencyContext',
    'CurrencyException',
    'CurrencyInvalidDivision',
    'CurrencyInvalidMultiplication',
    'CurrencyInvalidOperation',
    'CurrencyMismatchException',
    'CurrencyTypeException',
    'DEFAULT_PRECISION',
    'DEFAULT_ROUNDING',
    'Afghani',
    'AlgerianDinar',
    'ArgentinePeso',
    'ArmenianDram',
    'ArubanFlorin',
    'AustralianDollar',
    'AustralianDollarAU',
    'AustralianDollarCC',
    'AustralianDollarKI',
    'AustralianDollarMR',
    'AustralianDollarTV',
    'AzerbaijanianManat',
    'BahamianDollar',
    'BahrainiDinar',
    'Baht',
    'Balboa',
    'BarbadosDollar',
    'BelarusianRuble',
    'BelizeDollar',
    'BermudianDollar',
    'BolivarFuerte',
    'Boliviano',
    'BrazilianReal',
    'BruneiDollar',
    'BruneiDollarBN',
    'BruneiDollarSG',
    'BulgarianLev',
    'BurundiFranc',
    'CFAFrancBCEAO',
    'CFAFrancBCEAOBF',
    'CFAFrancBCEAOBJ',
    'CFAFrancBCEAOCI',
    'CFAFrancBCEAOGW',
    'CFAFrancBCEAOML',
    'CFAFrancBCEAONG',
    'CFAFrancBCEAOSN',
    'CFAFrancBCEAOTG',
    'CFAFrancBEAC',
    'CFAFrancBEACCD',
    'CFAFrancBEACCF',
    'CFAFrancBEACCM',
    'CFAFrancBEACGA',
    'CFAFrancBEACGQ',
    'CFAFrancBEACTD',
    'CFPFranc',
    'CFPFrancNC',
    'CFPFrancPF',
    'CFPFrancWF',
    'CanadianDollarEN',
    'CanadianDollarFR',
    'CapeVerdeEscudo',
    'CaymanIslandsDollar',
    'Cedi',
    'ChileanPeso',
    'ColombianPeso',
    'CongoleseFranc',
    'CordobaOro',
    'CostaRicanColon',
    'CroatianKuna',
    'CubanPeso',
    'CzechKoruna',
    'Dalasi',
    'DanishKrone',
    'Denar',
    'DjiboutiFranc',
    'Dobra',
    'DominicanPeso',
    'Dong',
    'EasternCaribbeanDollar',
    'EasternCaribbeanDollarAG',
    'EasternCaribbeanDollarAI',
    'EasternCaribbeanDollarDM',
    'EasternCaribbeanDollarGD',
    'EasternCaribbeanDollarKN',
    'EasternCaribbeanDollarLC',
    'EasternCaribbeanDollarMS',
    'EasternCaribbeanDollarVC',
    'EgyptianPound',
    'EthiopianBirr',
    'Euro',
    'EuroAD',
    'EuroAT',
    'EuroBE',
    'EuroCY',
    'EuroDE',
    'EuroEE',
    'EuroES',
    'EuroFI',
    'EuroFR',
    'EuroGR',
    'EuroIE',
    'EuroIT',
    'EuroLT',
    'EuroLU',
    'EuroLV',
    'EuroMC',
    'EuroME',
    'EuroMT',
    'EuroNL',
    'EuroPT',
    'EuroSBA',
    'EuroSI',
    'EuroSK',
    'EuroSM',
    'EuroVA',
    'EuroXK',
    'FalklandIslandsPound',
    'FijiDollar',
    'Forint',
    'GibraltarPound',
    'Gourde',
    'Guarani',
    'GuineaFranc',
    'GuyanaDollar',
    'HongKongDollar',
    'Hryvnia',
    'IcelandKrona',
    'IndianRupee',
    'IndianRupeeBT',
    'IndianRupeeIN',
    'IranianRial',
    'IraqiDinar',
    'JamaicanDollar',
    'JordanianDinar',
    'KenyanShilling',
    'Kina',
    'Kip',
    'KonvertibilnaMarka',
    'KuwaitiDinar',
    'Kwacha',
    'Kwanza',
    'Kyat',
    'Lari',
    'LebanesePound',
    'Lek',
    'Lempira',
    'Leone',
    'Leu',
    'LiberianDollar',
    'LibyanDinar',
    'Lilangeni',
    'Loti',
    'MalagasyAriary',
    'MalaysianRinggit',
    'Manat',
    'MauritiusRupee',
    'Metical',
    'MexicanPeso',
    'MoldovanLeu',
    'MoroccanDirham',
    'Naira',
    'Nakfa',
    'NamibiaDollar',
    'NepaleseRupee',
    'NewIsraeliShekel',
    'NewIsraeliShekelIL',
    'NewIsraeliShekelPS',
    'NewZealandDollar',
    'NewZealandDollarCK',
    'NewZealandDollarNU',
    'NewZealandDollarNZ',
    'NewZealandDollarPN',
    'Ngultrum',
    'NorthKoreanWon',
    'NorwegianKrone',
    'NuevoSol',
    'Ouguiya',
    'PZloty',
    'Paanga',
    'PakistanRupee',
    'Pataca',
    'PesoUruguayo',
    'PhilippinePeso',
    'PoundSterling',
    'PoundSterlingGB',
    'PoundSterlingGG',
    'PoundSterlingIM',
    'PoundSterlingIO',
    'Pula',
    'QatariRial',
    'Quetzal',
    'Rand',
    'RandLS',
    'RandNA',
    'RandZA',
    'RialOmani',
    'Riel',
    'Rufiyaa',
    'Rupiah',
    'RussianRuble',
    'RussianRubleGE',
    'RussianRubleRU',
    'RwandaFranc',
    'SaintHelenaPound',
    'SaudiRiyal',
    'SerbianDinarSR',
    'SerbianDinarXK',
    'SeychellesRupee',
    'SingaporeDollar',
    'SingaporeDollarBN',
    'SingaporeDollarSG',
    'SolomonIslandsDollar',
    'Som',
    'SomaliShilling',
    'Somoni',
    'SouthKoreanWon',
    'SriLankaRupee',
    'SudanesePound',
    'SurinameDollar',
    'SwedishKrona',
    'SwissFranc',
    'SwissFrancCH',
    'SwissFrancLI',
    'SyrianPound',
    'TaiwanDollar',
    'Taka',
    'Tala',
    'TanzanianShilling',
    'Tenge',
    'TrinidadandTobagoDollar',
    'Tugrik',
    'TunisianDinar',
    'TurkishLira',
    'TurkishLiraCY',
    'TurkishLiraTR',
    'UAEDirham',
    'USDollar',
    'USDollarAS',
    'USDollarFM',
    'USDollarGU',
    'USDollarHT',
    'USDollarIO',
    'USDollarMH',
    'USDollarMP',
    'USDollarPA',
    'USDollarPC',
    'USDollarPR',
    'USDollarPW',
    'USDollarTC',
    'USDollarVG',
    'USDollarVI',
    'UgandaShilling',
    'UzbekistanSum',
    'Vatu',
    'YemeniRial',
    'Yen',
    'Yuan',
    'ZambianKwacha',
    'ZimbabweDollar',
    'Bitcoin',
    'EOS',
    'Ethereum',
    'Monero',
    'Ripple',
    'StellarLumens',
    'Tezos',
    'Zcash']


__author__: str = 'Frederico Martins'
__license__: str = 'MIT'
__project__: str = __package__
__version__: str = '1.0.1'

# add private classes to the doc
__pdoc__ = {}
__pdoc__['multicurrency._exceptions'] = True
__pdoc__['multicurrency._currency'] = True
