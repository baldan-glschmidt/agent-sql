# E140MTR

## Descrição

Vendas - Notas Fiscais de Saída - Modal de Transporte

---

## Resumo

- Campos: 19
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqMtr | Number(004,0) | Não | Sequência (ordem) do modal |
| CodVia | String(003) | Não | Código da via de transportes |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade |
| CidIni | String(060) | Não | Cidade de início do modal |
| UfsIni | String(002) | Não | Sigla do estado referente ao local de início do modal |
| CepFim | Number(008,0) | Sim | Faixa final do CEP da cidade |
| CidFim | String(060) | Não | Cidade de término do modal |
| UfsFim | String(002) | Não | Sigla do estado referente ao local de término do modal |
| CodTra | Number(009,0) | Sim | Código da Transportadora responsável pelo modal |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqMtr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140MTR_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

