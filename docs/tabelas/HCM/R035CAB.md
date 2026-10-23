# R035CAB

## Descrição

PPP - Dados Administrativos

---

## Resumo

- Campos: 39
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição |
| NumCgc | Number(015,0) | Sim | Número da Inscrição - Obsoleto |
| CfjIns | String(014) | Sim | Número da Inscrição |
| RazSoc | String(040) | Sim | Razão Social da Filial |
| AtiIrf | Number(007,0) | Sim | CNAE Fiscal |
| CodFil | Number(006,0) | Sim | Código da Filial |
| EndFil | String(040) | Sim | Endereço da Filial |
| CodCep | Number(008,0) | Sim | Código do CEP da Filial |
| NomBai | String(040) | Sim | Nome do Bairro da Filial |
| NomCid | String(030) | Sim | Nome da Cidade da Filial |
| EstCid | String(002) | Sim | Estado da Cidade da Filial |
| NomFun | String(040) | Sim | Nome do Colaborador |
| IndPDH | String(003) | Sim | BR/PDH |
| NITFun | Number(011,0) | Sim | NIT do Funcionário |
| DatNas | Date | Sim | Data de Nascimento |
| TipSex | String(001) | Sim | Sexo do Colaborador |
| NumCtp | Number(009,0) | Sim | Número da Carteira de Trabalho |
| SerCtp | String(005) | Sim | Série da Carteira de Trabalho |
| EstCtp | String(002) | Sim | UF da Carteira de Trabalho |
| DatAdm | Date | Sim | Data de Admissão |
| DesRev | String(030) | Sim | Descrição do Regime de revezamento |
| NomRRH | String(040) | Sim | Nome do Representante legal da Empresa |
| NITRRH | Number(011,0) | Sim | NIT do Representante legal |
| CpfRRH | Number(011,0) | Sim | CPF do Representante legal |
| JusCat | String(200) | Sim | Justificativa para constar no campo CAT do  PPP |
| JusExa | String(200) | Sim | Justificativa para não informar exames no PPP |
| JusAss | String(200) | Sim | Justificativa para uso de assinatura eletrônica no PPP |
| JusGer | String(3000) | Sim | Justificativa geral para constar antes data emissão do  PPP |
| UltUsu | Number(010,0) | Sim | Responsável pela última alteração |
| ProAtu | String(001) | Sim | Profissiografia Atualizada |
| ProFec | String(001) | Sim | Profissiografia Fechada |
| RisAtu | String(001) | Sim | Riscos Atualizados |
| RisFec | String(001) | Sim | Riscos Fechados |
| CarRRH | String(060) | Sim | Cargo do representante legal |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| MatEso | String(030) | Sim | Matrícula eSocial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
