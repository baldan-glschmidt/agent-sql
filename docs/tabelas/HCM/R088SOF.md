# R088SOF

## Descrição

Solicitações de Oficina

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSol | Number(006,0) | Não | Código da Solicitação de Oficina |
| PlaVei | String(010) | Sim | Placa do Veículo |
| DatSol | Date | Sim | Data da Solicitação do Veículo |
| HorSol | Number(005,0) | Sim | Hora da Solicitação do Veículo |
| EmpSol | Number(004,0) | Sim | Código da Empresa do Solicitante da Solicitação |
| TipSol | Number(001,0) | Sim | Tipo do Solicitante |
| CadSol | Number(009,0) | Sim | Cadastro do Solicitante |
| DatLib | Date | Sim | Data da Liberação do Veículo para Manutenção |
| HorLib | Number(005,0) | Sim | Hora Liberação do Veículo para Manutenção |
| DatCon | Date | Sim | Data da Conclusão do Veículo na Manutenção |
| HorCon | Number(005,0) | Sim | Hora Conclusão do Veículo na Manutenção |
| StaSol | Number(001,0) | Sim | Status Solicitação |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador da Solicitação |
| TipAut | Number(001,0) | Sim | Tipo Autorizador da Solicitação |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador da Solicitação |
| ObsSol | String(300) | Sim | Observação da Solicitação |

---

## Chave Primária

- CodSol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088SOF_001

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

