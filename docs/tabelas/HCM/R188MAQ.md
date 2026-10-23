# R188MAQ

## Descrição

PLR - Máquinas

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodMaq | Number(004,0) | Não | Código da Máquina |
| DesMaq | String(030) | Sim | Descrição da Máquina |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CodMaq

---

## Índices

### R188MAQIndice2

**Tipo:** Não unico

Campos:
- NumLoc

---

## Relacionamentos

### IR_R188MAQ_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

