# R088LVO

## Descrição

Liberação Veículos da Oficina

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatLib | Date | Não | Data da Liberação |
| HorLib | Number(005,0) | Não | Hora da Liberação |
| EmpRes | Number(004,0) | Sim | Código da Empresa Responsável pela Entrada |
| TclRes | Number(001,0) | Sim | Tipo de Colaborador Responsável pela Entrada |
| CadRes | Number(009,0) | Sim | Cadastro do Autorizador Responsável pela Entrada |
| NumOrs | Number(007,0) | Sim | Número da Ordem de Serviço |

---

## Chave Primária

- PlaVei
- DatLib
- HorLib

---

## Índices

### R088LVOIndice2

**Tipo:** Não unico

Campos:
- PlaVei

---

## Relacionamentos

### IR_R088LVO_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

