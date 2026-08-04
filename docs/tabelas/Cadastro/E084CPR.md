# E084CPR

## Descrição

Cadastros - Máscara Produto - Componentes

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMpr | String(008) | Não | Código  da Máscara Derivação |
| CodCpr | String(014) | Não | Código do Componente da Máscara de Produto |
| SeqCpr | Number(009,0) | Não | Número  Sequencial  dos componentes da máscara |
| DesCpr | String(050) | Não | Descrição do Componente da Máscara |
| AbrCpr | String(020) | Não | Abreviatura do Componente da Máscara |
| CodAgr | Number(004,0) | Sim | Código do agrupamento p/ Produto. |
| SitCpr | String(001) | Não | Situação do componente da máscara de produto |

---

## Chave Primária

- CodEmp
- CodMpr
- CodCpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E084CPR_001

**Tabela:** E084MPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpr | CodMpr |

