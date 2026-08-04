# E070CTB

## Descrição

Cadastros - Filiais - Parâmetros Contabilidade

---

## Resumo

- Campos: 29
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CtbCff | Number(007,0) | Sim | Classificação Nacional de Atividade Econômica da Empresa (CNAE Fiscal) |
| EndCtd | String(100) | Sim | Endereço do contador |
| NumCtd | Number(005,0) | Sim | Número do endereço do contador |
| CplCtd | String(020) | Sim | Complemento do endereço do contador (sala, andar, etc.) |
| CepCtd | Number(008,0) | Sim | CEP do contador |
| BaiCtd | String(075) | Sim | Bairro do contador |
| CidCtd | String(060) | Sim | Cidade do contador |
| UfsCtd | String(002) | Sim | Sigla do estado do contador |
| FonCtd | String(020) | Sim | Número do telefone do contador |
| FaxCtd | String(020) | Sim | Número do FAX do contador |
| IntNet | String(100) | Sim | Endereço eletrônico do contador (E-Mail) |
| PerCta | String(001) | Sim | Permitir lançamento contábil com mesma conta a débito e a crédito |
| PerCon | Date | Sim | Período Final de Conciliação dos Saldos Contábeis |
| DiaLct | Number(001,0) | Sim | Dia permitido para data do lançamento contábil |
| RatPde | String(001) | Sim | Permite alterar rateio do tipo pré-definido sem confirmação |
| GerSpd | String(001) | Sim | Indicativo que a filial é informada para a geração do SPED |
| LctSlt | String(001) | Sim | Permitir a geração de lançamento contábil manual sem lote |
| ForCtb | Number(001,0) | Sim | Indicativo da consistência aplicada na contabilização dos lotes contábeis |
| LotSti | String(001) | Sim | Permitir a contabilização de lote contábil sem total informado |
| DatDlt | String(001) | Sim | Permitir lançamento com data em competência diferente do lote |
| NumCgc | Number(014,0) | Sim | Número do cadastro nacional de pessoa jurídica do escritório de contabilidade |
| DocIdeCon | String(014) | Sim | Número do cadastro nacional de pessoa jurídica do escritório de contabilidade |
| NomCtb | String(100) | Sim | Nome do escritório de contabilidade da empresa |
| NatPes | Number(004,0) | Sim | Natureza da Pessoa Juridica |
| PstCtd | Number(006,0) | Sim | Número da caixa postal |
| CpsCtd | Number(008,0) | Sim | Código de endereçamento postal da caixa postal |
| CtbFim | Date | Sim | Data Final das atividades da empresa |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070CTB_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E070CTB_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

