# R015DLI

## Descrição

Direito da Licença Especial

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| DiaFal | Number(003,0) | Não | Dias de Faltas |
| DiaDir | Number(004,0) | Sim | Dias de Direito |
| MaxPrr | Number(004,0) | Sim | Máximo Dias Prorrogação |

---

## Chave Primária

- CodSin
- DiaFal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R015DLI_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

