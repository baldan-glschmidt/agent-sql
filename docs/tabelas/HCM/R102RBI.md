# R102RBI

## Descrição

Reuniões da Brigada - Imagens

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodBri | Number(003,0) | Não | Código da Brigada |
| DatReu | Date | Não | Data da Reunião |
| HorReu | Number(005,0) | Não | Hora da Reunião |
| SeqImg | Number(003,0) | Não | Sequência de imagem |
| DesImg | String(030) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Imagem |

---

## Chave Primária

- NumEmp
- CodBri
- DatReu
- HorReu
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102RBI_001

**Tabela:** R102BRI

| Origem | Destino |
|--------|---------|
| CodBri | CodBri |

