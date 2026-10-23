# R088TRV

## Descrição

Troca de Veículos Usuários

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatTro | Date | Não | Data da Troca do Veículo |
| HorTro | Number(005,0) | Não | Hora da Troca |
| EmpRes | Number(004,0) | Sim | Código da Empresa Responsável pela Troca |
| TclRes | Number(001,0) | Sim | Tipo de Colaborador Responsável pela Troca |
| CadRes | Number(009,0) | Sim | Cadastro do Autorizador Responsável pela Troca |
| NovPlv | String(010) | Sim | Nova Placa do Veículo |

---

## Chave Primária

- PlaVei
- DatTro
- HorTro

---

## Índices

### R088TRVIndice2

**Tipo:** Não unico

Campos:
- NovPlv
- DatTro

---

## Relacionamentos

### IR_R088TRV_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088TRV_006

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| NovPlv | PlaVei |

