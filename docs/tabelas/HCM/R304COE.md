# R304COE

## Descrição

e-Sfinge Online - Especialidades do Concurso/Processo Seletivo

---

## Resumo

- Campos: 34
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| NumEsp | Number(006,0) | Não | Número da Especialidade |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CarFun | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| DatIni | Date | Não | Data de Início da Vigência do Cargo |
| SeqReg | Number(009,0) | Não | Sequência |
| DscEsp | String(100) | Não | Descrição da Especialidade |
| DatHom | Date | Sim | Data da Homologação |
| DscHab | String(255) | Sim | Descrição da Habilitação |
| VagOfe | Number(006,0) | Não | Quantidade de Vagas Oferecidas para Ampla Concorrência |
| VagDef | Number(006,0) | Sim | Quantidade de Vagas reservadas a Portadores de Deficiência |
| VagAfr | Number(006,0) | Sim | Quantidade de Vagas reservadas a Afrodescendentes |
| VagInd | Number(006,0) | Sim | Quantidade de Vagas reservadas a Índios |
| TipDis | Number(002,0) | Não | Tipo de Distribuição das Vagas |
| LocDis | String(255) | Sim | Local de Distribuição das Vagas |
| CadRes | String(001) | Não | Indicativo de Formação de Cadastro de Reserva |
| IdaMax | Number(002,0) | Sim | Idade máxima permitida para admissão |
| NotCor | Number(007,4) | Sim | Nota de Corte para Aprovação |
| TipEsc | Number(002,0) | Não | Escolaridade |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| PidSta | String(030) | Sim | Pid Status |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(008,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(008,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Number(008,0) | Sim | Campo Auxiliar 5 |
| CmpAu6 | Number(008,0) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(002) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(002) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(2000) | Sim | Campo Auxiliar 9 |
| IndHom | String(001) | Sim | Indicativo homologação parcial |
| IndBar | String(001) | Sim | Indicativo de cláusula de barreira |

---

## Chave Primária

- NumEmp
- NumEdi
- NumEsp
- TipQua
- CarFun
- DatIni
- SeqReg

---

## Índices

### R304COEIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
