# E140ISM

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Seviço - Mensagens

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqIsm | Number(009,0) | Não | Sequencia |
| CodEmp | Number(004,0) | Não | Código da empresa da nota fiscal de saída |
| CodFil | Number(005,0) | Não | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIsv | Number(003,0) | Não | Sequência do item de serviço da nota fiscal de saída |
| CodMsg | Number(004,0) | Não | Código da mensagem do item de serviço da nota fiscal de saída |
| MsgIsm | String(1000) | Não | Texto da mensagem do item de serviço da nota fiscal de saída |

---

## Chave Primária

- SeqIsm

---

## Índices

### E140ISMItemNotaFiscal

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIsv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
