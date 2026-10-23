# R030FIL

## Descrição

Filiais da Empresa

---

## Resumo

- Campos: 130
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| RazSoc | String(040) | Sim | Razão Social da Filial |
| NomFil | String(040) | Sim | Apelido da Filial |
| AtvFil | String(080) | Sim | Atividade da Filial |
| CplFil | String(040) | Sim | Complemento Endereço |
| TipLgr | String(005) | Sim | Tipo de Logradouro |
| EndFil | String(040) | Sim | Endereço da Filial |
| EndNum | String(006) | Sim | Número |
| CodPai | Number(004,0) | Sim | Código do País |
| CodEst | String(004) | Sim | Estado |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| CodBai | Number(004,0) | Sim | Código do Bairro |
| CodCep | Number(008,0) | Sim | Código do Cep da Filial |
| TipFil | String(001) | Sim | Tipo Filial (M,F,O,T, C, D) |
| RecFgt | Number(001,0) | Sim | Recolhimento FGTS (0,1,2) |
| CenFgt | Number(006,0) | Sim | Centralizadora do FGTS |
| CatFgt | Number(002,0) | Sim | Categoria FGTS |
| CdrFgt | Number(003,0) | Sim | Código de Recolhimento do Fgts (GFIP) |
| NatEst | Number(004,0) | Sim | Natureza Jurídica RAIS |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição da Filial |
| NumCgc | Number(015,0) | Sim | Número da Inscrição |
| CfjCgc | String(014) | Sim | Número da Inscrição |
| InsCei | Number(012,0) | Sim | Código Inscrição CEI |
| EmpFgt | Number(013,0) | Sim | Empresa no FGTS |
| InsEst | String(015) | Sim | Inscrição Estadual |
| AtiIrf | Number(007,0) | Sim | CNAE Fiscal |
| AtiRai | Number(007,0) | Sim | Código Nacional de Atividade Econômica |
| BanFgt | Number(004,0) | Sim | Banco do FGTS |
| AgeFgt | Number(005,0) | Sim | Agência do FGTS |
| CodBan | Number(004,0) | Sim | Código do Banco |
| CodAge | Number(005,0) | Sim | Código da Agência |
| ConBan | Number(012,0) | Sim | Conta Bancária |
| DigBan | String(003) | Sim | Dígito Conta Banco |
| MotCgc | Number(001,0) | Sim | Motivo da Mudança de CNPJ |
| ProTra | Number(004,0) | Sim | Proprietários Trabalhando |
| FamTra | Number(002,0) | Sim | Familiares Trabalhando |
| FilCtb | Number(006,0) | Sim | Filial Contábil |
| IniAtv | Date | Sim | Início Atividades |
| EncAtv | Date | Sim | Encerramento Atividade |
| MudEnd | Date | Sim | Última Mudança Endereço |
| MudCgc | Date | Sim | Última Mudança Cnpj |
| UltFic | Number(009,0) | Sim | Última Ficha Registro Filial |
| TabFeD | Number(004,0) | Sim | Tabela de Feriados Diurna |
| TabFeN | Number(004,0) | Sim | Tabela de Feriados Noturna |
| FerOfD | Number(004,0) | Sim | Tabela de Feriados Diurna |
| FerOfN | Number(004,0) | Sim | Tabela de Feriados Noturna |
| BanPis | Number(004,0) | Sim | Código do Banco p/ Convênio do PIS |
| AcvPis | Number(005,0) | Sim | Agência Convênio PIS |
| AalPis | Number(005,0) | Sim | Agência Alternativa PIS |
| MotEnc | Number(001,0) | Sim | Motivo Encerramento Atividades |
| CgcAnt | Number(014,0) | Sim | CNPJ Anterior |
| CfjAnt | String(014) | Sim | CNPJ Anterior |
| RegDrt | Number(010,0) | Sim | Registro DRT |
| NumTel | String(020) | Sim | Telefone da Filial |
| NumFax | String(015) | Sim | Número do Fax da Filial |
| AutExt | String(001) | Sim | Autorização de Horas Extras |
| FecHEx | String(001) | Sim | Tipo de Fechamento das Horas Extras |
| LimHEx | Number(010,0) | Sim | Limite de Horas Extras por Colaborador |
| EmpCra | Number(004,0) | Sim | Empresa no Crachá de Colaborador |
| ViaCra | Number(002,0) | Sim | Via Inicial no Crachá do Colaborador |
| EmpPro | Number(004,0) | Sim | Empresa no Crachá Provisório de Colaborador |
| ViaPro | Number(001,0) | Sim | Via no Crachá Provisório de Colaborador |
| GraRis | Number(001,0) | Sim | Grau de Risco |
| EmpPcm | Number(004,0) | Sim | Código da empresa do responsável pelo PCMSO |
| TipRes | Number(001,0) | Sim | Tipo do Responsável pelo PCMSO |
| CadRes | Number(009,0) | Sim | Cadastro do Responsável pelo PCMSO |
| EmpFPD | Number(013,0) | Sim | Código da Empresa p/ Prazo Determinado |
| CodOem | Number(008,0) | Sim | Código do Tomador de Serviço |
| EmaFil | String(100) | Sim | Email da Filial |
| CodSvr | Number(003,0) | Sim | Código do Servidor |
| PerSen | Number(005,2) | Sim | Esse campo foi descontinuado, agora é utilizado o campo R030GRP.PerSen |
| JunHor | String(001) | Sim | Juntar Horas Diurnas/Noturnas cfe Turno do Horário |
| EncPrv | Number(004,2) | Sim | % Encargos Provisões |
| ParPat | String(001) | Sim | Participante PAT |
| DatCna | Date | Sim | Data de alteração do CNAE Fiscal |
| EmpLau | Number(004,0) | Sim | Código da empresa do responsável pelo LTCAT |
| TipLau | Number(001,0) | Sim | Tipo do Responsável pelo LTCAT |
| CadLau | Number(009,0) | Sim | Cadastro do Responsável pelo LTCAT |
| EmpRrh | Number(004,0) | Sim | Código da empresa do responsável área de RH |
| TipRrh | Number(001,0) | Sim | Tipo do Responsável pela área de RH |
| CadRrh | Number(009,0) | Sim | Cadastro do Responsável pela área de RH |
| SitOrc | String(001) | Sim | Orçamento fechado p/manutenção |
| CodIdn | Number(015,0) | Sim | Código de identificação da filial |
| DatAEx | Number(001,0) | Sim | Funcionamento da Data na Autorização de Extras |
| TpCtBa | Number(001,0) | Sim | Tipo Conta |
| NomCom | String(100) | Sim | Nome Empresarial Completo |
| EmpPPP | Number(004,0) | Sim | Código da empresa do responsável pelo PPP |
| TipPPP | Number(001,0) | Sim | Tipo do Responsável pelo PPP |
| CadPPP | Number(009,0) | Sim | Cadastro do Responsável pelo PPP |
| CgcCsi | Number(015,0) | Sim | CNPJ Centralizadora Contribuição Sindical |
| CfjCsi | String(014) | Sim | CNPJ Centralizadora Contribuição Sindical |
| FilSin | String(001) | Sim | Filial Sindicalizada |
| CtlFic | String(001) | Sim | Controle Ficha Registro |
| CtlFil | Number(006,0) | Sim | Filial Controle |
| CnaPre | String(001) | Sim | CNAE Preponderante |
| GerCEs | String(001) | Sim | Calcular o DSR Conforme os Dias de DSR da Escala |
| JusExa | String(200) | Sim | Justificativa para não informar exames no PPP |
| JusCat | String(200) | Sim | Justificativa para constar no campo CAT do  PPP |
| JusAss | String(200) | Sim | Justificativa para uso de assinatura eletrônica no PPP |
| JusGer | String(3000) | Sim | Justificativa geral p/ constar antes data emissão do  PPP |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| DddFax | Number(003,0) | Sim | Código DDD do Fax |
| DdiFax | Number(003,0) | Sim | Código DDI do Fax |
| NumSeg | String(025) | Sim | Número do seguro social |
| InsMun | String(016) | Sim | Inscrição Municipal da Filial |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| BanHor | Number(004,0) | Sim | Código do Totalizador Banco de Horas |
| BanFix | String(001) | Sim | Período de Banco Horas Fixo |
| MesPer | Number(002,0) | Sim | Quantidade de meses do período do banco de horas |
| IniVig | Date | Sim | Início Vigência p/ Ano Base |
| FimVig | Date | Sim | Fim Vigência p/ Ano Base |
| BlqAdm | Number(001,0) | Sim | Bloqueia admissões no Adm de Pessoal quando integrado ao Recrutamento e Seleção |
| CgcBdc | Number(015,0) | Sim | CNPJ de integração BDCC |
| CfjBdc | String(014) | Sim | CNPJ de integração BDCC |
| CpfBdc | Number(011,0) | Sim | CPF de integração BDCC |
| LotBdc | Number(002,0) | Sim | Lote para o BDCC |
| LogBdc | String(100) | Sim | Login para a conexão com o BDCC |
| SenBdc | String(100) | Sim | Senha para a conexão com o BDCC |
| NumCNO | Number(012,0) | Sim | Inscrição no CNO |
| NCAEPF | Number(014,0) | Sim | Inscrição no CAEPF |
| TipLot | Number(002,0) | Sim | Tipo de lotação da filial |
| CnaFis | Number(007,0) | Sim | CNAE Fiscal Preponderante |
| TipCae | Number(001,0) | Sim | Tipo CAEPF |
| PgMDsr | Number(002,0) | Sim | Pagar multa por trabalho no DSR |
| TpcPix | Number(002,0) | Sim | Tipo de Chave Pix - Pagamento Instantâneo |
| ChvPix | String(100) | Sim | Chave Pix - Pagamento Instantâneo |
| FusMar | Number(002,0) | Sim | Fuso Horário |
| CpfRes | Number(011,0) | Sim | Número do CPF do responsável legal pelo Rep-P |

---

## Chave Primária

- NumEmp
- CodFil

---

## Índices

### R030FILIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- NomFil

### R030FILIndice3

**Tipo:** Não unico

Campos:
- CodCid
- CodBai

---

## Relacionamentos

### IR_R030FIL_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R030FIL_012

**Tabela:** R074BAI

| Origem | Destino |
|--------|---------|
| CodCid | CodCid |
| CodBai | CodBai |

