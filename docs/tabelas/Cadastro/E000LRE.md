# E000LRE

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Log

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CgcFil | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| DocIdeFil | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| CgcFor | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIdeFor | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| SeqLre | Number(009,0) | Não | Sequência do log rec. eletrônico |
| TipIte | Number(001,0) | Sim | Tipo de log |
| SeqIte | Number(006,0) | Não | Sequência do item relacionado |
| DesLre | String(9999) | Sim | Descrição do log |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeNfc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000LREIndice1

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel
- SeqLre

### E000LREIndice2

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel
- SeqLre

### E000LREIndice3

**Tipo:** Não unico

Campos:
- IdeNfc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
