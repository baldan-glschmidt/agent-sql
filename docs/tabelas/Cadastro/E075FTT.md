# E075FTT

## Descrição

Cadastros - Produtos - Texto Descritivo Técnico (Fotos)

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| FotPro | String(014) | Não | Código da foto do produto |
| FotDer | String(007) | Não | Código da Derivação da foto |
| SeqFot | Number(004,0) | Não | Sequência  da  Foto do produto |
| SeqFtt | Number(004,0) | Não | Sequência do texto |
| DesFtt | String(240) | Não | Descrição do Texto - informativos e/ou detalhes técnicos |
| DatAlt | Date | Sim | Data da alteração do Registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do Registro |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou o Registro |

---

## Chave Primária

- CodEmp
- FotPro
- FotDer
- SeqFot
- SeqFtt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E075FTT_003

**Tabela:** E075FOT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| FotPro | FotPro |
| FotDer | FotDer |
| SeqFot | SeqFot |

