# R088MFL

## Descrição

Movimento Veículos Frota com Acesso Livre

---

## Resumo

- Campos: 18
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatEnt | Date | Não | Data de Entrada |
| HorEnt | Number(005,0) | Não | Hora de Entrada |
| EmpUsu | Number(004,0) | Sim | Código da Empresa do Usuário do Veículo |
| TclUsu | Number(001,0) | Sim | Tipo de Colaborador Usuário do Veículo |
| CadUsu | Number(009,0) | Sim | Cadastro do Usuário do Veículo |
| CadOcr | Number(009,0) | Sim | Cadastro do Colaborador de Outra Unidade |
| ObsMov | String(080) | Sim | Observação do Movimento |
| EmpRes | Number(004,0) | Sim | Código da Empresa Responsável pela Entrada |
| TclRes | Number(001,0) | Sim | Tipo de Colaborador Responsável pela Entrada |
| CadRes | Number(009,0) | Sim | Cadastro do Autorizador Responsável pela Entrada |
| DatSai | Date | Sim | Data da Saída da Empresa |
| HorSai | Number(005,0) | Sim | Hora da Saída da Empresa |
| PorEnt | Number(003,0) | Sim | Código da Portaria da Entrada |
| PorSai | Number(003,0) | Sim | Código da Portaria da Saída |
| EmpSai | Number(004,0) | Sim | Código da Empresa Responsável pela Saída |
| TclSai | Number(001,0) | Sim | Tipo do Responsável pela Saída |
| CadSai | Number(009,0) | Sim | Cadastro do Responsável pela Saída |

---

## Chave Primária

- PlaVei
- DatEnt
- HorEnt

---

## Índices

### R088MFLIndice2

**Tipo:** Não unico

Campos:
- PlaVei

---

## Relacionamentos

Nenhum relacionamento cadastrado.
