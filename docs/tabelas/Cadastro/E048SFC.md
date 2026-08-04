# E048SFC

## Descrição

Tabelas - Formas de Contabilização - Itens

---

## Resumo

- Campos: 34
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFct | String(005) | Não | Código da forma de contabilização |
| SeqFct | Number(003,0) | Não | Sequência da forma de contabilização |
| OriFct | String(003) | Não | Módulo de origem da forma de contabilização |
| AnaSin | String(001) | Não | Indicativo se o lançamento contábil deve ser analítico ou sintético |
| SeqBfi | Number(006,0) | Sim | Critério de busca da filial |
| AbgFil | String(250) | Sim | Endereço de busca da filial |
| SeqBdt | Number(006,0) | Sim | Critério de busca da data |
| DatBas | String(250) | Sim | Endereço de busca da data base |
| SeqBcd | Number(006,0) | Sim | Critério de busca da conta de débito |
| CtaDeb | String(250) | Sim | Endereço de busca da conta de débito |
| SeqBcc | Number(006,0) | Sim | Critério de busca da conta de crédito |
| CtaCre | String(250) | Sim | Endereço de busca da conta de crédito |
| SeqBvl | Number(006,0) | Sim | Critério de busca do valor |
| VlrBas | String(250) | Sim | Endereço de busca do valor |
| CodHpd | Number(004,0) | Sim | Código do histórico padrão |
| SeqBcp | Number(006,0) | Sim | Critério de busca do complemento do histórico padrão |
| CplBas | String(250) | Sim | Endereço de busca do complemento do histórico padrão |
| SeqBcg | Number(006,0) | Sim | Critério de busca do CNPJ/CPF da conta débito |
| CgcCpf | String(250) | Sim | Endereço de busca do número do CNPJ ou CPF da conta débito |
| SeqBcr | Number(006,0) | Sim | Critério de busca do CNPJ/CPF da conta crédito |
| CgcCre | String(250) | Sim | Endereço de busca do número do CNPJ ou CPF da conta crédito |
| CodMoe | String(003) | Sim | Código da moeda para conversão |
| CodReg | Number(004,0) | Sim | Código da regra de cálculo |
| ObsSfc | String(250) | Sim | Observação do item da forma de contabilização |
| SeqRlc | Number(003,0) | Sim | Sequência da forma de contabilização relacionada |
| ObsCpl | String(250) | Sim | Endereço de busca da observação complementar |
| FtcUni | String(001) | Sim | Indica se a sequência ira gerar um novo fato contábil |
| UsuAlt | Number(010,0) | Sim | Código do usuário responsável pelo alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| SeqBde | Number(006,0) | Sim | Critério de busca da data do extemporâneo |
| DatExt | String(250) | Sim | Endereço de busca da data do extemporâneo |
| IndSnc | String(001) | Sim | Indica se a sequência irá atualizar durante a sincronização das Formas de Contabilização |

---

## Chave Primária

- CodEmp
- CodFct
- SeqFct

---

## Índices

### E048SFCIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFct
- SeqFct
- FtcUni

---

## Relacionamentos

### IR_E048SFC_001

**Tabela:** E048FCT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFct | CodFct |

