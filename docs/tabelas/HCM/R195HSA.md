# R195HSA

## Descrição

Cenário - Histórico Salarial

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatAlt | Date | Não | Data da Alteração |
| CodMot | Number(003,0) | Sim | Motivo da Alteração |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| ValSal | Number(013,4) | Sim | Salário Atual |
| CplSal | Number(013,4) | Sim | Valor Complementar ao Salário |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| PerRea | Number(008,5) | Sim | % de Reajuste Concedido |
| OriHsa | Number(001,0) | Sim | Origem do Histórico |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195HSA_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195HSA_005

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

