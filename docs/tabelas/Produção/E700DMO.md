# E700DMO

## Descrição

Ficha - Modelo - Derivações Possíveis

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto |
| CodDer | String(007) | Não | Código de Derivação associado ao Modelo |
| SeqCmd | Number(007,0) | Não | Sequência da Derivação na Máscara |
| PesLiq | Number(011,5) | Sim | Peso líquido do produto |
| PesBru | Number(011,5) | Sim | Peso bruto do produto |
| PreCus | Number(015,6) | Sim | Preço de custo |
| DatAlt | Date | Sim | Data da Geração do registro |
| CodUsu | Number(010,0) | Sim | Código do Usuário que alterou |

---

## Chave Primária

- CodEmp
- CodMod
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700DMO_001

**Tabela:** E700MOD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |

