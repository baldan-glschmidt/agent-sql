# R088MFA

## Descrição

Movimento Veículos Frota com Acesso Restrito

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
| AceNor | String(001) | Sim | Acessórios Normais |
| QuiEnt | Number(007,0) | Sim | Quilometragem do Veículo na Entrada |
| QuiSai | Number(007,0) | Sim | Quilometragem do Veículo na Saída |

---

## Chave Primária

- PlaVei
- DatEnt
- HorEnt

---

## Índices

### R088MFAIndice2

**Tipo:** Não unico

Campos:
- PlaVei

---

## Relacionamentos

Nenhum relacionamento cadastrado.
