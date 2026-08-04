# E000NEX

## Descrição

Gerais - Integração de notas fiscais de entrada com seniorX

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqItx | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| IdeUni | String(050) | Sim | Identificador único da nota fiscal de entrada na integração com seniorX |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |
| RnvItx | String(001) | Sim | Indicativo se deve reenviar a nota fiscal de entrada para integração com seniorX |

---

## Chave Primária

- SeqItx

---

## Índices

### E000NEXIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodFor
- CodSnf
- NumNfc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
