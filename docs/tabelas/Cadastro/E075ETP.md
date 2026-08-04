# E075ETP

## Descrição

Cadastros - Produtos - Especificações Técnicas Conformidade p/ Produtos

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto (Quando específico p/ cada derivação) |
| CodEct | String(014) | Não | Código da especificação técnica conformidade do produto |
| SeqCet | Number(004,0) | Não | Número da sequência de conformidade válido para o produto (quando automático do cadastro) |
| VlrCe1 | Number(015,6) | Sim | Valor alvo p/ conformidade do produto |
| VlrCe2 | Number(015,6) | Sim | Valor mínimo p/ conformidade do produto |
| VlrCe3 | Number(015,6) | Sim | Valor máximo p/ conformidade do produto |
| DesEct | String(050) | Sim | Descrição da especificação técnica de conformidade de produto |
| ObsEct | String(999) | Sim | Texto da observação da especificação técnica de conformidade de produto |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodEct
- SeqCet

---

## Índices

### E075ETPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodEct

---

## Relacionamentos

### IR_E075ETP_003

**Tabela:** E094ECT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEct | CodEct |

