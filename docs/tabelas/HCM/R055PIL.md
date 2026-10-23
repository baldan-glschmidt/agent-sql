# R055PIL

## Descrição

Planilha Integrada de Liquidação de Aportes(Colômbia)

---

## Resumo

- Campos: 59
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpPil | Date | Não | Competência |
| TipCot | Number(002,0) | Sim | Tipo Cotizante |
| NovIng | String(001) | Sim | Admissão |
| NovRet | String(001) | Sim | Rescisão |
| NovTde | String(001) | Sim | Transferência Saúde (Origem) |
| NovTae | String(001) | Sim | Transferência Saúde (Destino) |
| NovTdp | String(001) | Sim | Transferência Pensão (Origem) |
| NovTap | String(001) | Sim | Transferência Pensão (Destino) |
| NovVsp | String(001) | Sim | Alteração Salarial |
| NovVte | String(001) | Sim | Alteração Tarifa Especial |
| NovVst | String(001) | Sim | Alteração Salário Líquido |
| NovSln | String(001) | Sim | Licença Não Remunerada |
| NovIge | String(001) | Sim | Incapacidade Geral |
| NovLma | String(001) | Sim | Licença Maternidade |
| NovVac | String(001) | Sim | Férias |
| NovAvp | String(001) | Sim | Aporte Voluntário |
| NovVct | String(001) | Sim | Transferência de Filial |
| NovIrp | Number(002,0) | Sim | Acidente de Trabalho |
| PenOri | Number(008,0) | Sim | Administradora Pensão (Origem) |
| PenDes | Number(008,0) | Sim | Administradora Pensão (Destino) |
| SauOri | Number(008,0) | Sim | Administradora Saúde (Origem) |
| SauDes | Number(008,0) | Sim | Administradora Saúde (Destino) |
| CodCcf | Number(008,0) | Sim | Código CCF |
| DiaPen | Number(002,0) | Sim | Dias Considerados Pensão |
| DiaSau | Number(002,0) | Sim | Dias Considerados Saúde |
| DiaPer | Number(002,0) | Sim | Dias Considerados Periculosidade |
| SalBas | Number(011,2) | Sim | Salário Base |
| BasPen | Number(011,2) | Sim | Base Pensão |
| BasSau | Number(011,2) | Sim | Base Saúde |
| BasPer | Number(011,2) | Sim | Base Periculosidade |
| BasCCF | Number(011,2) | Sim | Base CCF |
| BasRef | Number(011,2) | Sim | Base Referência |
| TarPen | Number(007,4) | Sim | Tarifa Pensão |
| ConVol | Number(011,2) | Sim | Contribuição Voluntária Pensão (Colaborador) |
| ConEmp | Number(011,2) | Sim | Contribuição Voluntária Pensão (Empresa) |
| ConSol | Number(011,2) | Sim | Contribuição Solidariedade |
| ConSub | Number(011,2) | Sim | Contribuição Subsistência |
| ValNRc | Number(011,2) | Sim | Valor Não Recolhido |
| TarSau | Number(007,4) | Sim | Tarifa Saúde |
| AdiSau | Number(011,2) | Sim | Contribuição Adicional Saúde |
| AutInc | String(015) | Sim | Nº Autorização Incapacidade |
| ValInc | Number(011,2) | Sim | Valor Incapacidade |
| AutMat | String(015) | Sim | Nº Autorização Maternidade |
| ValMat | Number(011,2) | Sim | Valor Maternidade |
| TarPer | Number(007,4) | Sim | Tarifa Periculosidade |
| CodCct | Number(009,0) | Sim | Código do Centro de Trabalho |
| TarCCF | Number(007,4) | Sim | Tarifa CCF |
| TarSEN | Number(007,4) | Sim | Tarifa SENA |
| TarICB | Number(007,4) | Sim | Tarifa ICBF |
| TarESA | Number(007,4) | Sim | Tarifa ESAP |
| TarEDU | Number(007,4) | Sim | Tarifa Ministério Educação |
| SalLiq | Number(011,2) | Sim | Salário Líquido |
| AdmPer | Number(008,0) | Sim | Administradora Riscos |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| StaReg | Number(001,0) | Sim | Indica o status do registros |
| DatAlt | Date | Sim | Data da geração/alteração do registro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
