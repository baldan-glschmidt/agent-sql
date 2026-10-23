# R088VEO

## Descrição

Veículos dos Colaboradores de Outra Unidade

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| NumEmp | Number(004,0) | Não | Empresa Proprietária do Veículo |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |

---

## Chave Primária

- PlaVei
- NumEmp
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088VEO_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088VEO_002

**Tabela:** R070OCR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| NumCad | NumCad |

