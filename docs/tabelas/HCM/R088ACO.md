# R088ACO

## Descrição

Acompanhantes Veículos de Teste

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| MarVei | String(015) | Não | Marca do Veículo |
| ModVei | String(015) | Não | Modelo do Veículo |
| NumCha | String(020) | Não | Número do Chassi |
| DatLib | Date | Não | Data da Liberação |
| HorLib | Number(005,0) | Não | Hora da Liberação |
| EmpCon | Number(004,0) | Não | Código da Empresa do Condutor |
| TClCon | Number(001,0) | Não | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Não | Cadastro do Condutor |
| DatAco | Date | Sim | Data do Retorno do Acompanhante |
| HorAco | Number(005,0) | Sim | Hora do Retorno do Acompanhante. |

---

## Chave Primária

- MarVei
- ModVei
- NumCha
- DatLib
- HorLib
- EmpCon
- TClCon
- CadCon

---

## Índices

### R088ACOIndice2

**Tipo:** Não unico

Campos:
- EmpCon
- TClCon
- CadCon

---

## Relacionamentos

### IR_R088ACO_000

**Tabela:** R088MAR

| Origem | Destino |
|--------|---------|
| MarVei | MarVei |

### IR_R088ACO_001

**Tabela:** R088MOD

| Origem | Destino |
|--------|---------|
| MarVei | MarVei |
| ModVei | ModVei |

### IR_R088ACO_004

**Tabela:** R088PVT

| Origem | Destino |
|--------|---------|
| MarVei | MarVei |
| ModVei | ModVei |
| NumCha | NumCha |
| DatLib | DatLib |
| HorLib | HorLib |

