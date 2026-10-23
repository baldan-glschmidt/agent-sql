# R088REC

## Descrição

Reclamações de Veículos

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatRec | Date | Não | Data da Reclamação |
| HorRec | Number(005,0) | Não | Hora da Reclamação |
| DatOcr | Date | Sim | Data do Ocorrido |
| HorOcr | Number(005,0) | Sim | Hora do Ocorrido |
| EmpCon | Number(004,0) | Sim | Empresa do Colaborador Condutor do Veículo |
| TipCon | Number(001,0) | Sim | Tipo de Condutor da Frota |
| CadCon | Number(009,0) | Sim | Cadastro do Colabolador Condutor do Veículo |
| DesRec | String(080) | Sim | Descrição da Reclamação |
| QtdPon | Number(002,0) | Sim | Quantidade de Pontos para o Condutor do Veículo |
| NomRec | String(040) | Sim | Nome do Reclamante |
| TelRec | String(020) | Sim | Número do Telefone do Reclamante |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |

---

## Chave Primária

- PlaVei
- DatRec
- HorRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088REC_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

